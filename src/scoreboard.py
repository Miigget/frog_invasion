import pygame.font


class Scoreboard():
    """A class to report scoring information"""

    def __init__(self, fi_settings, screen, stats):
        """Initialize scorekeeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.fi_settings = fi_settings
        self.stats = stats

        # font settings for scoring info
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare the initial score image
        self.prep_score()

    
    def prep_score(self):
        """Turn score into rendered image"""
        # rounded_score = int(round(self.stats.score, -1)) rounds score to nearest 10
        # score_str = "{:,}".format(rounded_score)
        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.fi_settings.bg_color)

        # display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)