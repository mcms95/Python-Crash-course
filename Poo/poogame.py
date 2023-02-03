# main

import sys
import pygame

from settings import Settings
from time import sleep
from toilet import Toilet
from paper import Paper
from poo import Poo
from game_stats import GameStats


class PooGame:
    """Main class, manages everything"""

    def __init__(self):
        """Star game"""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        # Windows size (set in settings)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Poo")

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.toilet = Toilet(self)
        self.bullets = pygame.sprite.Group()
        self.poos = pygame.sprite.Group()
        self._poo_army()

        # Start Poo in an active state.
        self.game_active = True

    def run_game(self):
        """Start main loop for the game"""
        while True:
            self._check_events()
            if self.game_active:
                self.toilet.update()
                self._update_bullets()
                self._update_poos()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        """Update images on screen"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.toilet.blitme()
        self.poos.draw(self.screen)

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def _check_events(self):
        # Respond to keypresses and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # If key is pressed create motion
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # If key is not pressed stop motion
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        """Responds to key releases"""
        # If stop pressing right
        if event.key == pygame.K_RIGHT:
            self.toilet.moving_right = False
        # If stop pressing left
        elif event.key == pygame.K_LEFT:
            self.toilet.moving_left = False

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            # Move ship to the right
            self.toilet.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move ship to the left
            self.toilet.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """Create paper and add it to the ammo."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Paper(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update paper position and remove extra"""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_poo_collisions()

    def _check_bullet_poo_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.poos, True, True)

        if not self.poos:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _create_poo(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_poo = Poo(self)
        new_poo.x = x_position
        new_poo.rect.x = x_position
        new_poo.rect.y = y_position
        self.poos.add(new_poo)

    def _poo_army(self):
        """Create an army of poo."""
        # Create an poo and keep adding poo until there's no room left.
        # Spacing between poos is one poo width and one poo height.
        # Make an poo.
        poo = Poo(self)
        poo_width, poo_height = poo.rect.size

        current_x, current_y = poo_width, poo_height
        while current_y < (self.settings.screen_height - 2 * poo_height):
            while current_x < (self.settings.screen_width - 2 * poo_width):
                self._create_poo(current_x, current_y)
                current_x += 2 * poo_width
            # Finished a row; reset x value, and increment y value.
            current_x = poo_width
            current_y += 2 * poo_height

    def _update_poos(self):
        """Check if the army is at an edge, then update positions."""
        self._check_army_edges()
        self.poos.update()

        # Look for poo-toilet collisions.
        if pygame.sprite.spritecollideany(self.toilet, self.poos):
            self._toilet_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_poos_bottom()

    def _check_army_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for poo in self.poos.sprites():
            if poo.check_edges():
                self._change_army_direction()
                break

    def _change_army_direction(self):
        """Drop the entire army and change the army's direction."""
        for alien in self.poos.sprites():
            alien.rect.y += self.settings.army_drop_speed
        self.settings.army_direction *= -1

    def _toilet_hit(self):
        """Respond to the toilet being hit by an poo."""
        if self.stats.toilets_left > 0:
            # Decrement ships_left.
            self.stats.toilets_left -= 1

            # Get rid of any remaining bullets and  aliens.
            self.bullets.empty()
            self.poos.empty()

            # Create a new fleet and center the ship.
            self._poo_army()
            self.toilet.center_toilet()

            # Pause.
            sleep(0.5)
        else:
            self.game_active = False

    def _check_poos_bottom(self):
        """Check if any poos have reached the bottom of the screen."""
        for poo in self.poos.sprites():
            if poo.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the toilet got hit.
                self._toilet_hit()
                break


if __name__ == '__main__':
    # Make a game instance and run the game.
    game = PooGame()
    game.run_game()
