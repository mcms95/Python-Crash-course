class GameStats:
    """Track statistics for Poo."""

    def __init__(self, poo_game):
        """Initialize statistics."""
        self.settings = poo_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.toilets_left = self.settings.toilet_limit
