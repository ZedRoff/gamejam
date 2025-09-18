import arcade
from model.Button import Button
from model.ScenarioTitle import ScenarioTitle
from utils import getWindowSize
from model.BD import BD
from model.dialog import Dialog
"""





           

            
           
"""
class BdView(arcade.View):
    cycles = 0
    def __init__(self, fromClass):
        super().__init__()
        self.scene = None
        self.frames = []
        self.current_frame_index = 0
        self.frame_timer = 0
        self.frame_delay = 0 
        self.button_list = arcade.SpriteList()
        self.show_bd = True
        self.active_frame = None 
        self.fromClass = fromClass

    def setup(self):
        self.scene = arcade.Scene()
        width, height = getWindowSize.func()
        if self.fromClass == "laby":
            
            BdView.cycles = BdView.cycles + 1 
            if BdView.cycles == 3:
                self.frames = [
                    BD(0,0,"./assets/bg_1_4.png", delay=1, clear=True),
        
                BD(width // 2, height // 2, "./assets/bg_1_0.png", delay=0.1),
                    BD(width // 2, height // 2, "./assets/bg_1_2.png", delay=1),
                    BD(width // 2, height // 2, "./assets/bg_1_1.png", delay=1),
            
                BD(width // 2, height // 2, "./assets/fin_mvt_1.png", delay=1,should_be_deleted=True),
                BD(width // 2, height // 2, "./assets/fin_mvt_2.png", delay=1,should_be_deleted=True),
                BD(width // 2, height // 2, "./assets/fin_mvt_3.png", delay=1,should_be_deleted=True),
                BD(width // 2, height // 2, "./assets/fin_mvt_3.png", delay=1,should_be_deleted=True),
                
            BD(width // 2, height // 2, "./assets/fin_mvt_4.png", delay=1,should_be_deleted=True),
                

                ]
            else:
                self.frames = [
                    
            BD(width // 2, height // 2, "./assets/couloir_layout.png", delay=0.1),
              BD(width // 2, height // 2, "./assets/couloir_character1.png", delay=1),
       
            BD(width // 2, height // 2, "./assets/couloir_armoire_0.png", delay=1, should_be_deleted=True),
       
            BD(width // 2, height // 2, "./assets/couloir_armoire_1.png", delay=1, should_be_deleted=True),
            BD(width // 2, height // 2, "./assets/couloir_armoire_2.png", delay=1),
              ]
            
        if self.fromClass == "menu":
            self.frames = [
                 BD(width // 2, height // 2, "./assets/bg_1_0.png", delay=1),
            BD(width // 2, height // 2, "./assets/bg_1_1.png", delay=1, should_be_deleted=True),
            BD(width // 2, height // 2, "./assets/bg_1_2.png", delay=1),
            BD(width // 2, height // 2, "./assets/bg_1_3.png", delay=1, should_be_deleted=True),
            BD(width // 2, height // 2, "./assets/bg_1_4.png", delay=1, should_be_deleted=True),
            BD(width // 2, height // 2, "./assets/bg_1_5.png", delay=1, should_be_deleted=True),
            BD(width // 2, height // 2, "./assets/bg_1_6.png", delay=1, should_be_deleted=True),
            BD(width // 2, height // 2, "./assets/bg_1_7.png", delay=1),
            BD(width // 2, 250, "./assets/dialogue.png", delay=3, should_be_deleted=True, text="Parfait, ils sont partis dormir"),
            
                   
           BD(0,0,"./assets/bg_1_4.png", delay=1, clear=True),
           
            BD(width // 2, height // 2, "./assets/spe_0.png", delay=0.5),
            
            BD(width // 2, height // 2, "./assets/spe_1.png", delay=.5),
            
            BD(width // 2, height // 2, "./assets/spe_2.png", delay=.5),
            
            BD(width // 2, height // 2, "./assets/spe_3.png", delay=.5),
            
            BD(width // 2, height // 2, "./assets/spe_4.png", delay=.5),
            
            BD(width // 2, height // 2, "./assets/spe_5.png", delay=.5),
            
            BD(width // 2, height // 2, "./assets/spe_6.png", delay=.5),
            
            BD(width // 2, height // 2, "./assets/spe_7.png", delay=.5),
            
            BD(width // 2, height // 2, "./assets/spe_8.png", delay=.5),
            
            BD(width // 2, height // 2, "./assets/spe_9.png", delay=.5),
            
            BD(width // 2, height // 2, "./assets/spe_10.png", delay=.5),
            
            BD(width // 2, height // 2, "./assets/spe_11.png", delay=.5),
            
            
            
           BD(0,0,"./assets/bg_1_4.png", delay=2, clear=True),
           
            

            BD(width // 2, height // 2, "./assets/couloir_layout.png", delay=0.1),
             BD(width // 2, height // 2, "./assets/couloir_character1.png", delay=1),
            BD(width // 2, height // 2, "./assets/couloir_door_0.png", delay=1, should_be_deleted=True),

             BD(width // 2, height // 2, "./assets/couloir_door_1.png", delay=1),
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
            if self.active_frame.clear:
                self.scene["UI"].clear()
            if BdView.cycles == 3 and self.current_frame_index == len(self.frames)-1:
                print("fin du jeu")
                from views.menu_view import MenuView
                menu_view = MenuView()
                menu_view.setup()
                self.window.show_view(menu_view)
                return
            self.current_frame_index += 1

            if self.current_frame_index < len(self.frames):
                next_frame = self.frames[self.current_frame_index]
                self.active_frame = next_frame
                self.frame_delay = next_frame.delay
                self.scene.add_sprite("UI", self.active_frame)

            else:
                
                print("Fin des BD frames")
                
                from views.main_view import MainView
                game_view = MainView()
                 
                self.window.show_view(game_view)
                


    def on_show_view(self):
        print("Passage dans la BD")

    def on_key_press(self, symbol, modifiers):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        for button in self.button_list:
            if button.collides_with_point((x, y)):
                button.on_click()
