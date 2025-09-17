import arcade
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

class Hand:
    def __init__(self, hand_filename, direction, maze):
        self.image = arcade.Sprite(hand_filename, 1)
        self.image.width = 0.8 * SCREEN_WIDTH
        self.image.height = 0.8 * SCREEN_HEIGHT
        self.direction = direction
        self.maze = maze
        self.image_list = arcade.SpriteList()
        self.image_list.append(self.image)
        self.is_moving = False
        self.vitesse = 5
        
        center_y = self.maze.start_y + (self.maze.height_cases // 2) * self.maze.case_size
        
        if self.direction == "droite":
            self.image.center_x = SCREEN_WIDTH + self.image.width // 2
            self.target_x = self.maze.start_x + self.maze.width_cases * self.maze.case_size +700
        else:
            self.image.center_x = -self.image.width // 2
            self.target_x = self.maze.start_x+100
            
        self.image.center_y = center_y+100

    def start_movement(self):
        self.is_moving = True

    def update(self):
        if self.is_moving:
            if self.direction == "droite":
                if self.image.center_x > self.target_x:
                    self.image.center_x -= self.vitesse
                else:
                    self.is_moving = False
            else:
                if self.image.center_x < self.target_x:
                    self.image.center_x += self.vitesse
                else:
                    self.is_moving = False

    def draw(self):
        self.image_list.draw()