import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """Initialize game, settings and create a screen object"""

    pygame.init()
    fi_settings = Settings()
    screen = pygame.display.set_mode((fi_settings.screen_width, fi_settings.screen_height))
    pygame.display.set_caption("Frog Invasion")

    ship = Ship(fi_settings, screen)

    # Group to store bullets
    bullets = Group()

    # start the main loop for the game
    while True:

        gf.check_events(fi_settings, screen, ship, bullets)

        ship.update()
        bullets.update()

        # get rid of bullets that have disappeared
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        
        gf.update_screen(fi_settings, screen, ship, bullets)

run_game()