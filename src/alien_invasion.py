import sys
import pygame

from settings import Settings

def run_game():
    """Initialize game, settings and create a screen object"""

    pygame.init()
    fi_settings = Settings()
    screen = pygame.display.set_mode((fi_settings.screen_width, fi_settings.screen_height))
    pygame.display.set_caption("Frog Invasion")

    # start the main loop for the game
    while True:

        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(fi_settings.bg_color)

        # make the most recently drawn screen visible
        pygame.display.flip()

run_game()