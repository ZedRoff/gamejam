import arcade

class AngerBar:
    def __init__(self, x, y, width, height, max_value=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_value = max_value
        self.current_value = 0
        
        try:
            self.background_sprite = arcade.Sprite("assets/AgaceBar.png")
            self.background_sprite.width = width
            self.background_sprite.height = height
            self.background_sprite.center_x = x + width // 2
            self.background_sprite.center_y = y + height // 2
            self.image_loaded = True
            print("Image AgaceBar.png chargée avec succès")
        except Exception as e:
            print(f"Erreur lors du chargement de l'image: {e}")
            self.image_loaded = False
            self.background_sprite = None

        if self.background_sprite:
            self.background_list = arcade.SpriteList()
            self.background_list.append(self.background_sprite)
        
    def draw(self):
        self.background_list.draw()
        
        fill_percentage = self.current_value / self.max_value
        
        if fill_percentage > 0:
            margin_left = 10
            margin_right = 50
            available_width = self.width - margin_left - margin_right
            fill_width = fill_percentage * available_width
            
            bar_height = (self.y + self.height - 20 - 60) - (self.y + 20)
            bar_radius = bar_height // 2
            circle_center_x = self.x + margin_left + bar_radius
            circle_center_y = self.y + 20 + bar_radius
            
            if fill_width > 0:
                if fill_width >= bar_radius * 2:
                    arcade.draw_circle_filled(
                        circle_center_x,
                        circle_center_y,
                        bar_radius,
                        arcade.color.BLACK
                    )
                    
                    remaining_width = fill_width - (bar_radius * 2)
                    if remaining_width > 0:
                        arcade.draw_lrbt_rectangle_filled(
                            circle_center_x + bar_radius,
                            circle_center_x + bar_radius + remaining_width,
                            self.y + 20,
                            self.y + self.height - 20 - 60,
                            arcade.color.BLACK
                        )
                else:
                    arcade.draw_lrbt_rectangle_filled(
                        self.x + margin_left,
                        self.x + margin_left + fill_width,
                        self.y + 20,
                        self.y + self.height - 20 - 60,
                        arcade.color.BLACK
                    )
    
    def set_value(self, value):
        """Définir une valeur spécifique"""
        self.current_value = max(0, min(value, self.max_value))
    
    def increase(self, amount=5):
        """Augmenter la valeur"""
        self.set_value(self.current_value + amount)
        print(f"Barre d'agacement: {self.current_value}/{self.max_value} ({self.get_percentage():.1f}%)")
        
        if self.is_full():
            print("BARRE D'AGACEMENT PLEINE")
    
    def decrease(self, amount=5):
        """Diminuer la valeur"""
        self.set_value(self.current_value - amount)
    
    def get_percentage(self):
        """Obtenir le pourcentage de remplissage"""
        return (self.current_value / self.max_value) * 100
    
    def is_full(self):
        """Vérifier si la barre est pleine"""
        return self.current_value >= self.max_value
    
    def is_empty(self):
        """Vérifier si la barre est vide"""
        return self.current_value <= 0
    
    def reset(self):
        """Remettre la barre à zéro"""
        self.current_value = 0