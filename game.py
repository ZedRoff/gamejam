import arcade
from views.menu_view import MenuView

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_TITLE = "Game Jam"


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()
    
if __name__ == "__main__":
    main()