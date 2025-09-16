import arcade
from model.Button import Button
from model.MainTitle import MainTitle

from utils import getWindowSize
class ScenarioView(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = None
    def setup(self):
        self.scene = arcade.Scene()
    
        
    def on_draw(self):
        self.clear()
        self.scene.draw()
  
    def on_show_view(self):
        print("passage dans le scénario")
        
    def on_mouse_press(self, x, y, button, modifiers):
        pass
        
    