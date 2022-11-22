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
