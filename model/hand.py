import arcade
from ..utils.getWindowSize import func
class hand():
    def __init__(self,hand_filename,direction):
        self.image = arcade.Sprite(hand_filename, 1)
        width, height =func()
        self.image.width = 0.10*width
        self.image.height = 0.10* height
        self.image.center_x = 0.5*width
        self.image.center_y = 0.5*height
        self.direction = direction

    def deplacement(self,vitesse,limit):
        if self.direction=="droite":
            while(limit < self.image.center_x  ):
                self.image.center_x = self.image.center_x - vitesse
        else:
            while(limit > self.image.center_x  ):
                self.image.center_x = self.image.center_x + vitesse
            
    