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

    # Groups to store bullets and aliens
    bullets = Group()
    aliens = Group()

    # create the fleet of aliens
    gf.create_fleet(fi_settings, screen, ship, aliens)

    # start the main loop for the game
    while True:

        gf.check_events(fi_settings, screen, ship, bullets)

        ship.update()
        
        gf.update_bullets(bullets)

        gf.update_aliens(aliens)
        
        gf.update_screen(fi_settings, screen, ship, aliens, bullets)

run_game()