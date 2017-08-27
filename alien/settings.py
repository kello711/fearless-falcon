class Settings():
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # SHip settings
        self.ship_speed_factor = 5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 10
        self.fleet_drop_speed = 20
        # fleet direction of represents right; -1 represenets left
        self.fleet_direction = 1