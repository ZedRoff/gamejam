import arcade
from model.Button import Button
from model.MainTitle import MainTitle
from model.ScenarioTitle import ScenarioTitle

from utils import getWindowSize
class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = None
        self.button_list = arcade.SpriteList()
    def setup(self):
        self.scene = arcade.Scene()
        width, height = getWindowSize.func()
       

     
    def on_draw(self):
        self.clear()
        self.scene.draw()
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            print("appui") 
    def on_show_view(self):
        print("passage dans le jeu")
        
    def on_mouse_press(self, x, y, button, modifiers):
        for button in self.button_list:
            if button.collides_with_point((x,y)):
                button.on_click()
        
    