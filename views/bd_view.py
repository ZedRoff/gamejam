import arcade
from model.Button import Button
from model.ScenarioTitle import ScenarioTitle
from utils import getWindowSize
from model.BD import BD
from model.dialog import Dialog

class BdView(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = None
        self.frames = []
        self.current_frame_index = 0
        self.frame_timer = 0
        self.frame_delay = 0 
        self.button_list = arcade.SpriteList()
        self.show_bd = True
        self.active_frame = None 

    def setup(self):
        self.scene = arcade.Scene()
        width, height = getWindowSize.func()

        self.frames = [
            BD(width // 2, height // 2, "./assets/bg_1_0.png", delay=1),
            BD(width // 2, height // 2, "./assets/bg_1_1.png", delay=1, should_be_deleted=True),
            BD(width // 2, height // 2, "./assets/bg_1_2.png", delay=1),
            BD(width // 2, height // 2, "./assets/bg_1_3.png", delay=1, should_be_deleted=True),
            BD(width // 2, height // 2, "./assets/bg_1_4.png", delay=1, should_be_deleted=True),
            BD(width // 2, height // 2, "./assets/bg_1_5.png", delay=1, should_be_deleted=True),
            BD(width // 2, height // 2, "./assets/bg_1_6.png", delay=1, should_be_deleted=True),
            BD(width // 2, height // 2, "./assets/bg_1_7.png", delay=1, should_be_deleted=True),
            BD(width // 2, 250, "./assets/dialogue.png", delay=5, should_be_deleted=True, text="parfais, ils sont partis dormir"),
            BD(width // 2, height // 2, "./assets/bg_1_8.png", delay=3, should_be_deleted=True),
        ]

        self.active_frame = self.frames[0]
        self.frame_delay = self.frames[0].delay
        self.scene.add_sprite("UI", self.active_frame)

    def on_draw(self):
        self.clear()
        self.scene.draw()

        # Afficher le texte par-dessus la frame active
        if self.active_frame and self.active_frame.text:
            arcade.draw_text(
                self.active_frame.text,
                self.active_frame.center_x-350,
                self.active_frame.center_y+150,  # légèrement au-dessus
                arcade.color.BLACK,
                font_size=20,
                font_name="Arial",
                anchor_x="left",
                anchor_y="top"
            )

    def on_update(self, delta_time: float):
        if not self.show_bd:
            return

        self.frame_timer += delta_time

        if self.frame_timer >= self.frame_delay:
            self.frame_timer = 0

            # Supprimer la frame actuelle si nécessaire
            if self.active_frame and self.active_frame.should_be_deleted:
                self.scene["UI"].remove(self.active_frame)

            self.current_frame_index += 1

            if self.current_frame_index < len(self.frames):
                next_frame = self.frames[self.current_frame_index]
                self.active_frame = next_frame
                self.frame_delay = next_frame.delay
                self.scene.add_sprite("UI", self.active_frame)

            else:
                print("Fin des BD frames")
                self.show_bd = False
                from views.game_view import GameView
                game_view = GameView()
                game_view.setup()  
                self.window.show_view(game_view)


    def on_show_view(self):
        print("Passage dans la BD")

    def on_key_press(self, symbol, modifiers):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        for button in self.button_list:
            if button.collides_with_point((x, y)):
                button.on_click()
