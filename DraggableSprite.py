import arcade
class DraggableSprite:
    def __init__(self, sprite, sprite_list, collision_list=None):
        self.sprite = sprite
        self.sprite_list = sprite_list
        self.collision_list = collision_list
        self.dragged = False
        self.shake_counter = 0
        
    def on_mouse_press(self, x, y, button, modifiers):
        self.dragged = self.sprite.collides_with_point((x, y))
        
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.dragged:
            self.sprite.center_x += dx
            self.sprite.center_y += dy
            
            if self.collision_list:
                hit_list = arcade.check_for_collision_with_list(self.sprite, self.collision_list)
                if hit_list:
                    self.sprite.center_x -= dx
                    self.sprite.center_y -= dy
                    self.dragged = False
                    self.shake_counter = 20
    
    def update(self):
        if self.shake_counter > 0:
            if self.shake_counter % 4 == 0:
                self.sprite.angle = -15
            else:
                self.sprite.angle = 15
            self.shake_counter -= 1
            if self.shake_counter == 0:
                self.sprite.angle = 0