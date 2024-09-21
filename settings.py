class Settings():
    """
    A class to store all settings for Alien Invasion.
    """
    def __init__(self) -> None:
        """Initialize the game's static settings"""
        #screen settings
        self.screen_width = 1080
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed= 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #how quickly the game speed up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    
    def initialize_dynamic_settings(self):
        """
        Initialize settings that change throughout the game
        """
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        #fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #scoring setting
        self.alien_points = 50


    def increse_speed(self):
        """
        Increase speed settings
        """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale