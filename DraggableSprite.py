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
                    if hasattr(self.maze.view, 'anger_bar'):
                        self.maze.view.anger_bar.increase(20)  
            
            if self.other_objects_list:
                hit_objects = arcade.check_for_collision_with_list(self.sprite, self.other_objects_list)
                for obj in hit_objects:
                    if obj != self.sprite:
                        if hasattr(self.maze.view, 'anger_bar'):
                            self.maze.view.anger_bar.increase(20)  
                        collision = True
                        break
            
            if self.maze:
                maze_left = self.maze.start_x - 100
                maze_right = self.maze.start_x + self.maze.width_cases * self.maze.case_size + 100
                maze_bottom = self.maze.start_y - 100
                maze_top = self.maze.start_y + self.maze.height_cases * self.maze.case_size + 100
                
                if (self.sprite.center_x < maze_left or self.sprite.center_x > maze_right or
                    self.sprite.center_y < maze_bottom or self.sprite.center_y > maze_top):
                    
                    if hasattr(self.maze.view, 'hand_started') and not self.maze.view.hand_started:
                        print("La main n'est pas encore arrivée, impossible de changer de scène!")
                        self.sprite.center_x -= dx
                        self.sprite.center_y -= dy
                        self.dragged = False
                        return
                    
                    if hasattr(self.maze.view, 'active_hand') and self.maze.view.active_hand.is_moving:
                        print("La main est encore en mouvement, attendez qu'elle arrive!")
                        self.sprite.center_x -= dx
                        self.sprite.center_y -= dy
                        self.dragged = False
                        return
                    
                    hand_direction = self.maze.view.active_hand.direction if hasattr(self.maze.view, 'active_hand') else None
                    
                    object_exit_side = None
                    if self.sprite.center_x < maze_left:
                        object_exit_side = "gauche"
                    elif self.sprite.center_x > maze_right:
                        object_exit_side = "droite"
                    elif self.sprite.center_y < maze_bottom:
                        object_exit_side = "bas"
                    elif self.sprite.center_y > maze_top:
                        object_exit_side = "haut"
                    
                    if hand_direction and object_exit_side:
                        if (hand_direction == "gauche" and object_exit_side != "gauche") or \
                           (hand_direction == "droite" and object_exit_side != "droite"):
                            from views.bd_view import BdView
                            game_view = BdView("laby_spe")
                            game_view.setup()
                            print("Mauvais côté pour sortir l'objet!")
                            self.maze.view.window.show_view(game_view)
                            return
                        
                            self.sprite.center_x -= dx
                            self.sprite.center_y -= dy
                            self.dragged = False
                            return
                    
                    print(self.sprite.name)
                    if self.sprite.name == self.maze.random_item_image:
                        take = Music("take_object.wav", False)
                        take.play(1, False)
                        print("Correct item delivered!")
                    else:
                        print("Wrong item delivered!")
                        if hasattr(self.maze.view, 'anger_bar'):
                            self.maze.view.anger_bar.increase(20) 
                    
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