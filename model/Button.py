import arcade


class Button(arcade.Sprite):
    def __init__(self, title, x, y, image_path, scale, view):
        super().__init__(image_path, scale, opacity=100)
        self.center_x = x
        self.center_y = y
        self.title = title
        self.view = view

    def on_click(self):
        view_map = {
            "jouer": ("views.scenario_view", "ScenarioView"),
            "credits": ("views.credits_view", "CreditsView"),
            "back_from_scenario": ("views.menu_view", "MenuView"),
            "scenario_voleur": ("views.bd_view", "BdView")
        }

        if self.title == "quitter":
            arcade.close_window()
            return

        if self.title in view_map:
            module_path, class_name = view_map[self.title]

            module = __import__(module_path, fromlist=[class_name])
            view_class = getattr(module, class_name)
          
            if "BdView" in (str)(view_class):
                new_view = view_class("menu")
            else:
                new_view = view_class()
            if hasattr(new_view, "setup"):
                new_view.setup()
            self.view.window.show_view(new_view)
