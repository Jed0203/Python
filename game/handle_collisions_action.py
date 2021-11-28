import random
from game import constants
from game.action import Action
from game.dirt import Dirt
from game.obstacles import Obstacles

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self):
        self.counter = int(0)


    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        car = cast["car"][0]

        if cast["dirt_top"][0].center_x <= constants.MAX_X / 2 * -1:
            cast["dirt_top"].pop(0)
            cast["dirt_bottom"].pop(0)
            cast["dirt_top"][0].add_track(cast)
    
        try:
            if cast["obtacles"][0].center_x <= -20:
                cast["obstacles"][0].pop(0)
        except KeyError:
            pass
        
        go_slow = False
        for dirt in cast["dirt_top"]:
            if go_slow:
                break
            if self._handle_car_collision(car,dirt):
                go_slow = True

        for dirt in cast["dirt_bottom"]:
            if go_slow:
                break
            if self._handle_car_collision(car,dirt):
                go_slow = True
                break

        for obstacle in cast["obstacles"]:
            if go_slow:
                break
            if self._handle_car_collision(car, obstacle):
                go_slow = True

        if go_slow:
            for dirt in cast["dirt_top"]:
                dirt.change_x = -1
            for dirt in cast["dirt_bottom"]:
                dirt.change_x = -1
            for obstacle in cast["obstacles"]:
                obstacle.change_x = -1
            for item in cast["FINISH_LINE"]:
                item.change_x = -1
            
            self.counter += 1
        elif not go_slow:
            for dirt in cast["dirt_top"]:
                dirt.change_x = -5
            for dirt in cast["dirt_bottom"]:
                dirt.change_x = -5
            for obstacle in cast["obstacles"]:
                obstacle.change_x = -5
            for item in cast["FINISH_LINE"]:
                item.change_x = -5
            self.counter += 5

        if self.counter > constants.OBSTACLE_INTERVAL:
            cast["obstacles"].append(Obstacles())
            self.counter = 0

    def _handle_car_collision(self,car,the_object):
        return car.collides_with_sprite(the_object)
