import arcade
from model.Button import Button
from model.MainTitle import MainTitle
from model.Image import Image

from utils import getWindowSize
class CreditsView(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = None
        self.button_list = arcade.SpriteList()
    def setup(self):
        self.scene = arcade.Scene()
        w,h = getWindowSize.func()
        self.image = Image(w // 2, h // 2, "./assets/credits_bg.png", scale=0.7)
        self.scene.add_sprite("UI", self.image)
        width, height = getWindowSize.func()
        back_button = Button("back_from_scenario", 100, height-75,"./assets/back.png", 0.4, self)
        
        self.button_list.append(back_button)
        self.scene.add_sprite("UI", back_button)
    def on_draw(self):
        self.clear()
        self.scene.draw()
        
    def on_show_view(self):
        print("passage dans le menu")
        
    def on_mouse_press(self, x, y, button, modifiers):
        for button in self.button_list:
            if button.collides_with_point((x,y)):
                button.on_click()
        
    