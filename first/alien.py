import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """The class representing a single alien"""

    def __init__(self, ai_game):
        """Initialize the alien and create its initial position"""
        super().__init__()
        self.screen = ai_game.screen

