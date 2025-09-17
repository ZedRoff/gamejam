import arcade
import random
import arcade
import random
from Maze import Maze
from DraggableSprite import DraggableSprite
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Game Jam"

class MainView(arcade.View):
    def __init__(self):
        super().__init__()
        
        self.background_sprite = arcade.Sprite("assets/sacBack.png", scale=1)
        self.background_sprite.width = SCREEN_WIDTH - 1000
        self.background_sprite.height = SCREEN_HEIGHT
        self.background_sprite.center_x = SCREEN_WIDTH // 2 - 150
        self.background_sprite.center_y = SCREEN_HEIGHT // 2
        self.background_list = arcade.SpriteList()
       # self.background_list.append(self.background_sprite)
        
        self.maze = Maze(600//50, 600//50, 70, SCREEN_WIDTH//2-500, SCREEN_HEIGHT//2-450)
        self.maze.create_draggable_objects()

    def on_draw(self):
        self.clear()
        self.background_list.draw()
        self.maze.draw()

    def on_update(self, delta_time):
        self.maze.update()

    def on_key_press(self, symbol, modifiers):
        print(symbol)

    def on_mouse_press(self, x, y, button, modifiers):
        for draggable in self.maze.draggable_objects:
            draggable.on_mouse_press(x, y, button, modifiers)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        for draggable in self.maze.draggable_objects:
            draggable.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
    main_view = MainView()
    window.show_view(main_view)
    arcade.run()
    
if __name__ == "__main__":
    main()