from game import constants
from game.action import Action

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        # check = self._input_service.get_direction()
        # if not(check == "P"):
        direction = self._input_service.get_direction().scale(constants.CAR_MOVE_SCALE)
        car = cast["car"][0] # there's only one in the cast
        car.change_y = direction.get_y()
        if car.center_x >= constants.MAX_X- car.width/2:
            car.center_x = constants.MAX_X - car.width/2 -1
            car.change_x = 0
        elif car.center_x <= 0+car.width/2:
            car.center_x = 1+car.width/2
            car.change_x = 0
        else: 
            car.change_x = direction.get_x()

