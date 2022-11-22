import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """The class representing a single alien"""

    def __init__(self, ai_game):
        """Initialize the alien and create its initial position"""
        super().__init__()
        self.screen = ai_game.screen

        # Loading an Alien Image and assigning a rect attribute
        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()

        # Each new alien appears in the upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Preservation of the exact horizontal position of the alien.
        self.x = float(self.rect.x)