import arcade
class Dialog(arcade.Sprite):
    def __init__(self, x, y, delay, text="",should_be_deleted=False):
        super().__init__("./assets/dialogue.png", scale=0.1)
        self.center_x = x
        self.center_y = y
        self.text = text
        self.should_be_deleted = should_be_deleted
        self.delay = delay