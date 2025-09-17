import arcade
import random
from DraggableSprite import DraggableSprite
class Maze:
    def __init__(self, width_cases, height_cases, case_size=30, start_x=0, start_y=0):
        self.width_cases = width_cases
        self.height_cases = height_cases
        self.case_size = case_size
        self.start_x = start_x
        self.start_y = start_y
        self.sprite_list_mur = arcade.SpriteList()
        self.sprite_list_objects = arcade.SpriteList()
        self.draggable_objects = []
        self.G = self.generate_maze()
        self.create_walls()
    
    def generate_maze(self):
        G = [[1 for _ in range(self.width_cases)] for _ in range(self.height_cases)]
        center_y = self.height_cases // 2
        
        def carve(x, y):
            G[y][x] = 0 
            dirs = [(0, 2), (0, -2), (2, 0), (-2, 0)]
            random.shuffle(dirs)  
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 < nx < self.width_cases-1 and 0 < ny < self.height_cases-1 and G[ny][nx] == 1:
                    G[y + dy//2][x + dx//2] = 0  
                    carve(nx, ny)
        
        carve(center_y, 0)

        for i in range(self.height_cases):
            G[i][0] = 1
            G[i][self.width_cases-1] = 1
        for j in range(self.width_cases):
            G[0][j] = 1
            G[self.height_cases-1][j] = 1

        G[center_y][0] = 0  
        G[center_y][1] = 0                
        G[center_y][self.width_cases-1] = 0
        G[center_y][self.width_cases-2] = 0

        return G
    
    def get_wall_connections(self, i, j):
        up = i > 0 and self.G[i-1][j] == 1
        right = j < self.width_cases-1 and self.G[i][j+1] == 1  
        down = i < self.height_cases-1 and self.G[i+1][j] == 1
        left = j > 0 and self.G[i][j-1] == 1
        return (up, right, down, left)
    
    def get_wall_image(self, connections):
        #bas,droite,haut,gauche 
        wall_images = {
            (False, False, False, False): "assets/Block/4C.png",  
            (True, False, False, False): "assets/Block/b.png",       
            (False, True, False, False): "assets/Block/d.png",         
            (False, False, True, False): "assets/Block/h.png",      
            (False, False, False, True): "assets/Block/g.png",       
            (True, True, False, False): "assets/Block/db.png",       
            (True, False, True, False): "assets/Block/hb.png",       
            (False, True, True, False): "assets/Block/hd.png",       
            (False, True, False, True): "assets/Block/dg.png",       
            (False, False, True, True): "assets/Block/gh.png",      
            (True, True, True, False): "assets/Block/hbd.png",      
            (True, True, False, True): "assets/Block/bdg.png",      
            (True, False, True, True): "assets/Block/hbg.png",      
            (False, True, True, True): "assets/Block/hdg.png",   
            (True, False, False, True): "assets/Block/bg.png",  
            (True, True, True, True): "assets/Block/0C.png",      
        }
        return wall_images[connections]
    
    def create_walls(self):
        for i in range(len(self.G)):
            for j in range(len(self.G[i])):
                if self.G[i][j] == 1:
                    connections = self.get_wall_connections(i, j)
                    image_path = self.get_wall_image(connections)
                    
                    try:
                        mur = arcade.Sprite(image_path, 1)
                    except:
                        mur = arcade.Sprite("Block/4C.png", 1)
                    
                    mur.width = self.case_size
                    mur.height = self.case_size
                    mur.center_x = self.start_x + j * self.case_size
                    mur.center_y = self.start_y + i * self.case_size
                    self.sprite_list_mur.append(mur)
    
    def create_draggable_objects(self):
        object_images = ["assets/objects/cagoule.png", "assets/objects/biberon.png", "assets/objects/brosse_a_cheveux.png", "assets/objects/brosse_a_dent.png", "assets/objects/cadenas.png", "assets/objects/jouer_casser.png", "assets/objects/kit_de_crochetage.png"]
        
        empty_positions = []
        for i in range(len(self.G)):
            for j in range(len(self.G[i])):
                if self.G[i][j] == 0:
                    empty_positions.append((i, j))
        
        for i in range(7):
            pos = random.choice(empty_positions)
            empty_positions.remove(pos)

            obj = arcade.Sprite(object_images[i], 1)
            obj.width = 50
            obj.height = 50
            obj.center_x = self.start_x + pos[1] * self.case_size
            obj.center_y = self.start_y + pos[0] * self.case_size
            
            self.sprite_list_objects.append(obj)
            draggable = DraggableSprite(obj, self.sprite_list_objects, self.sprite_list_mur)
            self.draggable_objects.append(draggable)
    
    def update(self):
        for draggable in self.draggable_objects:
            draggable.update()
    
    def draw(self):
        self.sprite_list_mur.draw()
        self.sprite_list_objects.draw()