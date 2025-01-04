class Settings:
    """A class to store all game settings"""

    def __init__(self):
        """Initialize game settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 0.5

        # Bullet settings
        self.bullet_speed_factor = 0.3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 5
        self.fleet_direction = 1 # 1 represents moving right, -1 left