import pygame
from pygame.sprite import Sprite


class Poo(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, poo_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = poo_game.screen
        self.settings = poo_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/poo.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move poo right or left."""
        self.x += self.settings.poo_speed * self.settings.army_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if poo is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
