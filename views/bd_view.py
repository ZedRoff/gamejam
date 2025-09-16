import arcade
from model.Button import Button
from model.ScenarioTitle import ScenarioTitle
from utils import getWindowSize
class BdView(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = None
    def setup(self):
        self.scene = arcade.Scene()
        width, height = getWindowSize.func()
        title = ScenarioTitle(width // 2, height // 2 + 200)
        self.scene.add_sprite("UI", title)
    def on_draw(self):
        self.clear()
        self.scene.draw()
    
    def on_show_view(self):
        print("passage dans la BD")
    
    def on_mouse_press(self, x, y, button, modifiers):
        pass
        
    