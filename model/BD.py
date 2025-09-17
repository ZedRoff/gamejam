import arcade
class BD(arcade.Sprite):
    def __init__(self, x, y, image_path,delay, should_be_deleted=False):
        super().__init__(image_path, scale=0.3)
        self.center_x = x
        self.center_y = y
        self.should_be_deleted = should_be_deleted
        self.delay=delay
 