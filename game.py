import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_TITLE = "Game Jam"

class MainView(arcade.View):
    def __init__(self):
        super().__init__()
    def setup(self):
        pass
    def on_update(self, delta_time):
        pass
    def on_show_view(self):
        print("passage ici")
    def on_draw(self):
        arcade.draw_text("GAME JAM", SCREEN_WIDTH//2, SCREEN_HEIGHT//2, arcade.color.WHITE, 12, anchor_x='center')
    def on_key_press(self, symbol, modifiers):
        print(symbol)
    
def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
    main_view = MainView()
    window.show_view(main_view)
    arcade.run()
    
if __name__ == "__main__":
    main()