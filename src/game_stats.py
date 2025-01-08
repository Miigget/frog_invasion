class GameStats():
    """Track statistics for the game"""

    def __init__(self, fi_settings):
        """Initialize statistics"""
        self.fi_settings = fi_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.fi_settings.ship_limit
        self.score = 0