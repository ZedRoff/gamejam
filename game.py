import arcade
from views.menu_view import MenuView
from views.scenario_view import ScenarioView
import config
from utils import getWindowSize

def main():
    width, height = getWindowSize.func()
    window = arcade.Window(width, height, config.SCREEN_TITLE, resizable=False)
    arcade.set_background_color((252, 252, 252))
    menu_view = MenuView()
    menu_view.setup()
    window.show_view(menu_view)
    arcade.run()
    
if __name__ == "__main__":
    main()