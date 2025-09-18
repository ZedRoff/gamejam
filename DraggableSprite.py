import arcade
from model.Music import Music

class DraggableSprite:
    def __init__(self, sprite, sprite_list, collision_list=None, other_objects_list=None, maze=None):
        self.sprite = sprite
        self.sprite_list = sprite_list
        self.collision_list = collision_list
        self.other_objects_list = other_objects_list
        self.maze = maze
        self.dragged = False
        self.shake_counter = 0
        self.to_remove = False
        
    def on_mouse_press(self, x, y, button, modifiers):
        self.dragged = self.sprite.collides_with_point((x, y))
        
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.dragged:
            self.sprite.center_x += dx
            self.sprite.center_y += dy
            
            collision = False
            
            if self.collision_list:
                hit_list = arcade.check_for_collision_with_list(self.sprite, self.collision_list)
                if hit_list:
                    collision = True
                    # Augmenter la barre d'agacement de 1/5 (20%) quand mauvais objet
                    if hasattr(self.maze.view, 'anger_bar'):
                        self.maze.view.anger_bar.increase(20)  # 20% de la barre max (100)
            
            if self.other_objects_list:
                hit_objects = arcade.check_for_collision_with_list(self.sprite, self.other_objects_list)
                for obj in hit_objects:
                    if obj != self.sprite:
                        # Augmenter la barre d'agacement de 1/5 (20%) quand mauvais objet
                        if hasattr(self.maze.view, 'anger_bar'):
                            self.maze.view.anger_bar.increase(20)  # 20% de la barre max (100)
                        collision = True
                        break
            
            if self.maze:
                maze_left = self.maze.start_x - 100
                maze_right = self.maze.start_x + self.maze.width_cases * self.maze.case_size + 100
                maze_bottom = self.maze.start_y - 100
                maze_top = self.maze.start_y + self.maze.height_cases * self.maze.case_size + 100
                
                if (self.sprite.center_x < maze_left or self.sprite.center_x > maze_right or
                    self.sprite.center_y < maze_bottom or self.sprite.center_y > maze_top):
                    print(self.sprite.name)
                    if self.sprite.name  == self.maze.random_item_image:
                        take =Music("take_object.wav",False)
                        take.play(1,False)
                        print("Correct item delivered!")
                    else:
                        print("Wrong item delivered!")
                        # Augmenter la barre d'agacement de 1/5 (20%) quand mauvais objet
                        if hasattr(self.maze.view, 'anger_bar'):
                            self.maze.view.anger_bar.increase(20)  # 20% de la barre max (100)
                    
                    self.to_remove = True
                    self.sprite.remove_from_sprite_lists()
                    from views.bd_view import BdView
                    game_view = BdView("laby")
                    game_view.setup()
                    
                    self.maze.view.window.show_view(game_view)
                    return
            
            if collision:
                sound = Music("objet_toutch.wav", False)
                sound.play(1, False)
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