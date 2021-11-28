import arcade
import time
from pathlib import Path
from game import constants
from game.newtimer import Timer
import datetime

class Director(arcade.View):
    def __init__(self, cast, script, input_service):
        """Initialize the game
        """
        super().__init__()

        self._cast = cast
        self._script = script
        self._input_service = input_service
        self.total_time = 0.0
        self.timer = Timer()
        self._cast["timer"] = [self.timer]
        self.continues = True
        self.slow_music = None
        self.fileDir = Path(__file__).parent.parent
        self._sound_dictionary = {'engine':self.fileDir/'sounds/car.mp3','slow_engine':':resources:sounds/gameover2.wav'}

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.play_song()

    def on_update(self, delta_time):

        if len(self._cast['FINISH_LINE']) > 0:
            if self._cast['car'][0].collides_with_sprite(self._cast["FINISH_LINE"][0]):
                from game.endscreen import End_Menu
                end_view = End_Menu(self)
                self.window.show_view(end_view)
                
                
        if self.continues:
            #print("Q")
            self._cue_action("update")
            #print(self.total_time, delta_time)
            self.total_time += delta_time
            self.timer.timer_draw(self.total_time)

    def on_draw(self):
        self._cue_action("output")

    def on_key_press(self, symbol, modifiers):
        self._input_service.set_key(symbol, modifiers)

        if symbol == 112:
            from game.pause import Pause_Menu
            pause = Pause_Menu(self)
            self.window.show_view(pause)
        else:
            self._cue_action("input")

    def on_key_release(self, symbol, modifiers):
        self._input_service.remove_key(symbol, modifiers)
        self._cue_action("input")

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """
        for action in self._script[tag]:
            action.execute(self._cast)
            
    def play_song(self):
        """ Play the song. """
        # Stop what is currently playing.
        print('This works')
        if self.slow_music:
            self.slow_music.stop()
        self.slow_music = arcade.Sound(self._sound_dictionary['engine'], streaming = True)
        self.slow_music.play(volume=.3)
