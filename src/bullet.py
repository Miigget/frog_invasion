import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, fi_settings, screen, ship):
        """Create a bullet object at the ship's current position"""

        super().__init__()
        self.screen = screen

        # create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, fi_settings.bullet_width, fi_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = fi_settings.bullet_color
        self.speed_factor = fi_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen"""

        # update the decimal position of the bullet
        self.y -= self.speed_factor

        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)