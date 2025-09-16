import arcade

class Button(arcade.Sprite):

    def __init__(self,title, x, y, image_path, scale, view):
        super().__init__(image_path, scale)
        self.center_x = x
        self.center_y = y
        self.title = title
        self.view = view
    def on_click(self):
        if self.title == "quitter":
            arcade.close_window()
        elif self.title == "jouer":
            from views.bd_view import BdView 
            new_view = BdView()
            new_view.setup()
            self.view.window.show_view(new_view) 