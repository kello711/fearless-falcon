class Settings():
	"""A class to store all the settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# SHip Settings
		self.ship_speed_factor = 4.5

		# Bullet Settings
		self.bullet_speed_factor = 10
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3