import arcade
from model.Button import Button
from model.MainTitle import MainTitle

from utils import getWindowSize
class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = None
        self.button_list = None
        self.title = None
    def setup(self):
        self.scene = arcade.Scene()
        offset = -300
        title_offset = 300
        self.button_list = arcade.SpriteList()
        
        spacing = 125
        SCREEN_WIDTH,  SCREEN_HEIGHT = getWindowSize.func()
        self.title = MainTitle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + title_offset)
        self.scene.add_sprite("UI", self.title)
        titles = ["jouer", "parametres", "credits", "quitter"]
       
        for i in range(len(titles)): 
            start, end = (SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2) + offset + i * spacing
            title = titles[len(titles)-i-1]
            print(title)
            button = Button(title, start, end, f"./assets/{title}.png", 0.3, self)
            self.button_list.append(button)
            self.scene.add_sprite("UI", button)
        
    def on_draw(self):
        self.clear()
        self.scene.draw()
        
    def on_show_view(self):
        print("passage dans le menu")
        
    def on_mouse_press(self, x, y, button, modifiers):
        for button in self.button_list:
            if button.collides_with_point((x,y)):
                button.on_click()
        
    