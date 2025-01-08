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
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 0.3
        self.bullet_width = 1200
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 80
        self.fleet_direction = 1 # 1 represents moving right, -1 left

        # how quickly game speeds up
        self.speedup_scale = 1.1

        # how quickly alien point values increase
        self.score_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 0.5
        self.alien_speed_factor = 0.1
        self.fleet_direction = 1
        self.alien_points = 50 # scoring

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)