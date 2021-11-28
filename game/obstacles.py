from game.point import Point
from game import constants
from random import choice as choice
import arcade

class Obstacles(arcade.Sprite):
    def __init__(self):

        super().__init__(choice(constants.OBSTACLES_LIST))
        self.center_x = int(constants.MAX_X + 20)
        self.center_y = choice(range(int(constants.MAX_Y * 0.25),int(constants.MAX_Y * 0.75)))
        self.change_x = -5
        