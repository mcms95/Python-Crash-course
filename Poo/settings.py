class Settings:
    """Settings warehouse"""

    def __init__(self):
        """Game settings"""
        # Screen settings
        self.screen_width = 1500
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship(Toilet) settings
        self.toilet_speed = 5
        self.toilet_limit = 3

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6

        # Poo settings
        self.poo_speed = 1.0
        self.army_drop_speed = 10

        # fleet_direction of 1 represents right; -1 represents left.
        self.army_direction = 1
