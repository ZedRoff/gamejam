import arcade

class Music:

    def __init__(self,music_filename,long_file):
        self.background_music = arcade.Sound(music_filename, long_file)
        self.player = None
    
    def play(self,volume,loop):
        self.player = self.background_music.play(volume = volume,loop = loop)

    def pause(self):
        self.background_music.stop(self.player)

    def stop(self):
        arcade.stop_sound(self.player)