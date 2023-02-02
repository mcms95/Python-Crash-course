class Settings:
    """Settings warehouse"""

    def __init__(self):
        """Game settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 400
        self.bg_color = (230, 230, 230)

        # Ship(Toilet) settings
        self.ship_speed = 5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6
