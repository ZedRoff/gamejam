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
        self.background_sprite = None
        self.first_delay = 1
        self.first_timer = 0
    def setup(self):
        self.scene = arcade.Scene()
        width, height = getWindowSize.func()
        # Ajout du sprite de fond
        self.background_sprite = arcade.Sprite("assets/couloir_layout.png")  # Remplace par le chemin de ton image
        self.background_sprite.width = width
        self.background_sprite.height = height
        self.background_sprite.center_x = width // 2
        self.background_sprite.center_y = height // 2
        self.scene.add_sprite("Background", self.background_sprite)
        
        self.armory_sprite = arcade.Sprite("assets/armoire.png")
        self.armory_sprite.width = width
        self.armory_sprite.height = height
        self.armory_sprite.center_x = width // 2
        self.armory_sprite.center_y = height // 2
        self.scene.add_sprite("Foreground", self.armory_sprite)
        
        self.p_sprite = arcade.Sprite("assets/couloir_character1.png")
        self.p_sprite.width = width
        self.p_sprite.height = height
        self.p_sprite.center_x = width // 2
        self.p_sprite.center_y = height // 2
        self.scene.add_sprite("p", self.p_sprite)
        
        
        
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
        
    