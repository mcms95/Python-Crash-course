import sys
import pygame

from settings import Settings
from star import Star

class Stargame:
    """Class to manage game assets and behavior"""

    def __init__(self):
        """Start game and resources"""
        pygame.init()
        self.settings = Settings()
        
        pygame.display.set_caption("Star game")

        # Set the background
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        self.stars = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Start main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

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

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_star(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien.
        star = Star(self)
        star_width, star_height = star.rect.size
        current_x, current_y = star_width, star_height

        while current_y < (self.settings.screen_height - 3* star_height):
            while current_x < (self.settings.screen_width - 2 * star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width
            # Finished a row; reset x value, and increment y value.
            current_x = star_width
            current_y += 4 * star_height
    
            
            
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = Stargame()
    ai.run_game()