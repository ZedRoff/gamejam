import arcade
class Image(arcade.Sprite):
    def __init__(self, x, y, image_path, scale):
        super().__init__(image_path, scale)
        self.center_x = x
        self.center_y = y
 