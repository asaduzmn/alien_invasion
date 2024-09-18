class Settings():
    """
    A class to store all settings for Alien Invasion.
    """
    def __init__(self) -> None:
        """Initialize the game's settings"""
        #screen settings
        self.screen_width = 1080
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_speed_factor = 1.5