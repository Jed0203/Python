from game.action import Action
from game import constants
from game.newtimer import Timer

import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            _output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service
        #self.timer = Timer()

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()


        self._output_service.draw_actors(cast["dirt_top"])
        self._output_service.draw_actors(cast["dirt_bottom"])

        try:
            self._output_service.draw_actors(cast["obstacles"])
        except IndexError:
            pass
        
        try:
            self._output_service.draw_actor(cast["FINISH_LINE"][0])
        except IndexError:
            pass


        self._output_service.draw_actor(cast["car"][0])
        
        self._output_service.timer(cast["timer"][0].output)

        self._output_service.flush_buffer()

