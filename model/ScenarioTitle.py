import arcade
class ScenarioTitle(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("./assets/scenario.png", scale=1)
        self.center_x = x
        self.center_y = y
    