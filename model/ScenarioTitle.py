import arcade
class ScenarioTitle(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("./assets/jouer.png", scale=0.5)
        self.center_x = x
        self.center_y = y
 