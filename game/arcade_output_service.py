import sys
from game import constants

import arcade

class ArcadeOutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
        """
        pass
        
    def clear_screen(self):
        arcade.start_render()

    def draw_actor(self, actor):
        """Renders the given actor's text on the screen.

        Args:
            actor (Actor): The actor to render.
        """
        actor.draw()

    def draw_actors(self, actors):
        """Renders the given list of actors on the screen.

        Args:
            actors (list): The actors to render.
        """ 
        for actor in actors:
            self.draw_actor(actor)
    
    def flush_buffer(self):
        """Renders the screen.""" 
        pass
    
    def timer(self, output):
        arcade.draw_text(f'{str(output)}', 550, 550, arcade.color.BLACK, 30)

