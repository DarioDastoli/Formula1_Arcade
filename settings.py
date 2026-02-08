class Settings():
    """A class to manage all the settings for the application."""

    def __init__(self):
        # screen settings

        self.screen_width = 1200
        self.screen_height = 800

        # car settings
        self.rotation_speed = 0.1

        #color settings
        self.bg_color = (230, 230, 230)
        self.wall_color = (0,0,255)
        self.start_finish_color = (255,0,0)