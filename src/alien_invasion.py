import pygame

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

    # start the main loop for the game
    while True:

        gf.check_events(ship)

        ship.update()
        
        gf.update_screen(fi_settings, screen, ship)

run_game()