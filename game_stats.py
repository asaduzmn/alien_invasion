class GameStats:
    """
    Track statistics for Alien Invasion
    """
    def __init__(self, ai_game) -> None:
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        #start alien invasion in an active stat
        self.game_active = True


    def reset_stats(self):
        """
        Initializw statistics that can chage during the game
        """
        self.ships_left = self.settings.ship_limit