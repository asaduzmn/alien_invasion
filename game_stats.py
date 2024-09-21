class GameStats:
    """
    Track statistics for Alien Invasion
    """
    def __init__(self, ai_game) -> None:
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        #high score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """
        Initializw statistics that can chage during the game
        """
        self.ships_left = self.settings.ship_limit
        self.score = 0