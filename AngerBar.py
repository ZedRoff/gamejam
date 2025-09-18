import arcade

class AngerBar:
    def __init__(self, x, y, width, height, max_value=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_value = max_value
        self.current_value = 0
        
        self.background_sprite = arcade.Sprite("assets/AgaceBar.png")
        self.background_sprite.width = width
        self.background_sprite.height = height
        self.background_sprite.center_x = x + width // 2
        self.background_sprite.center_y = y + height // 2
        self.image_loaded = True

        if self.background_sprite:
            self.background_list = arcade.SpriteList()
            self.background_list.append(self.background_sprite)
        
    def draw(self):
        fill_percentage = self.current_value / self.max_value

        if fill_percentage > 0:
            fill_width = fill_percentage * self.width

            left = self.x
            right = self.x + fill_width
            bottom = self.y
            top = self.y + self.height

            arcade.draw_lrbt_rectangle_filled(
                left, right, bottom, top, arcade.color.WHITE
            )

        if self.image_loaded and self.background_sprite:
            self.background_list.draw()
        else:
            arcade.draw_rectangle_outline(
                self.x + self.width // 2,
                self.y + self.height // 2,
                self.width,
                self.height,
                arcade.color.BLACK,
                3
            )
    
    def set_value(self, value):
        """Définir une valeur spécifique"""
        self.current_value = max(0, min(value, self.max_value))
    
    def increase(self, amount=5):
        """Augmenter la valeur"""
        self.set_value(self.current_value + amount)
        print(f"Barre d'agacement: {self.current_value}/{self.max_value} ({self.get_percentage():.1f}%)")
        
        if self.is_full():
            print("BARRE D'AGACEMENT PLEINE ! Le joueur est au maximum de sa frustration !")
    
    def decrease(self, amount=5):
        """Diminuer la valeur"""
        self.set_value(self.current_value - amount)
    
    def get_percentage(self):
        return (self.current_value / self.max_value) * 100
    
    def is_full(self):
        return self.current_value >= self.max_value
    
    def is_empty(self):
        return self.current_value <= 0
    
    def reset(self):
        self.current_value = 0
