# main

import sys
import pygame

from settings import Settings
from toilet import Toilet
from paper import Paper
from poo import Poo


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
        self.toilet = Toilet(self)
        self.bullets = pygame.sprite.Group()
        self.poos = pygame.sprite.Group()
        self._poo_army()

    def run_game(self):
        """Start main loop for the game"""
        while True:
            self._check_events()
            self.toilet.update()
            self._update_bullets()
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

    def _create_poo(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_poo = Poo(self)
        new_poo.x = x_position
        new_poo.rect.x = x_position
        new_poo.rect.y = y_position
        self.poos.add(new_poo)

    def _poo_army(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        # Make an alien.
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



if __name__ == '__main__':
    # Make a game instance and run the game.
    game = PooGame()
    game.run_game()