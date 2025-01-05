import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    """Initialize game, settings and create a screen object"""

    pygame.init()
    fi_settings = Settings()
    screen = pygame.display.set_mode((fi_settings.screen_width, fi_settings.screen_height))
    pygame.display.set_caption("Frog Invasion")

    play_button = Button(fi_settings, screen, "PLAY")

    stats = GameStats(fi_settings)

    ship = Ship(fi_settings, screen)

    # Groups to store bullets and aliens
    bullets = Group()
    aliens = Group()

    # create the fleet of aliens
    gf.create_fleet(fi_settings, screen, ship, aliens)

    # start the main loop for the game
    while True:

        gf.check_events(fi_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:

            ship.update()
            
            gf.update_bullets(fi_settings, screen, ship, aliens, bullets)

            gf.update_aliens(fi_settings, stats, screen, ship, aliens, bullets)
        
        gf.update_screen(fi_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()