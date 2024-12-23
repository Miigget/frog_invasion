import pygame

class Ship:

    def __init__(self, fi_settings, screen):
        """Initialize the ship and set it's starting position"""
        self.screen = screen
        self.fi_settings = fi_settings

        # Load the ship image and get it's rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.fi_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.fi_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)