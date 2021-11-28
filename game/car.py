from game.point import Point
from game import constants

import arcade

class Car(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.CAR_IMAGE)

        self.center_x = int(constants.CAR_X)
        self.center_y = int(constants.MAX_Y / 2)
