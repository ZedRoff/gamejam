import arcade
class MainTitle(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("./assets/Sacre_sac.png", scale=0.5)
        self.center_x = x
        self.center_y = y
 