import arcade
class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
    def on_show_view(self):
        print("passage dans le menu")
        
    