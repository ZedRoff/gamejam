import arcade
from model.Button import Button
from model.MainTitle import MainTitle
from model.ScenarioTitle import ScenarioTitle

from utils import getWindowSize
class ScenarioView(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = None
        self.button_list = arcade.SpriteList()
    def setup(self):
        self.scene = arcade.Scene()
        width, height = getWindowSize.func()
        title = ScenarioTitle(width // 2, height // 2 + 400)
        self.scene.add_sprite("UI", title)
        # Position centrale
        x = width // 2
        y = height // 2
        spacing = 300  # Espace horizontal entre les boutons

        self.titles = ['scenario_politicien', 'scenario_voleur', 'scenario_clown']
        self.images = ['./assets/scenario_politicien.png', './assets/scenario_voleur.png', './assets/scenario_clown.png']
        self.descriptions = [
            ".",
            "Incarnez le sac d'un cambrioleur",
            "."
        ]

        # Calcul du point de départ (gauche) pour centrer les boutons
        start_x = x - spacing  # car 3 boutons → espacement sur 2 intervalles

        for i in range(3):
            button = Button(
                self.titles[i],
                start_x + i * spacing,  # 👈 variation horizontale
                y,                      # 👈 position verticale fixe
                self.images[i],
                0.8 if i==1 else 0.5,
                self
            )
            self.button_list.append(button)
            self.scene.add_sprite("UI", button)
        width, height = getWindowSize.func()
        back_button = Button("back_from_scenario", 100, height-75,"./assets/back.png", 0.4, self)
        self.button_list.append(back_button)
        self.scene.add_sprite("UI", back_button)

     
    def on_draw(self):
        self.clear()
        self.scene.draw()
        # Dessine la description sous chaque image de scénario
        x = getWindowSize.func()[0] // 2
        y = getWindowSize.func()[1] // 2
        spacing = 300
        start_x = x - spacing
        for i in range(3):
            desc_x = start_x + i * spacing
            desc_y = y - 350  # Ajuste selon la taille des images
            arcade.draw_text(
                self.descriptions[i],
                desc_x,
                desc_y,
                arcade.color.DARK_GRAY,
                font_size=14,
                anchor_x="center",
                anchor_y="top"
            )
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            print("appui") 
    def on_show_view(self):
        print("passage dans le scénario")
        
    def on_mouse_press(self, x, y, button, modifiers):
        for button in self.button_list:
            if button.collides_with_point((x,y)):
                button.on_click()
        
    