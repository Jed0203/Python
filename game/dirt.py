from game.point import Point
from game import constants

import arcade

class Dirt(arcade.Sprite):

    counter = 0

    def __init__(self,image_file):

        super().__init__(image_file)
        self.center_x = int(constants.MAX_X/2)
        self.center_y = int(constants.MAX_Y/2)
        self.change_x = -5
        Dirt.counter += 1
        print(Dirt.counter)
        self.finished = False

    def add_track(self,the_cast):
        the_cast["dirt_top"].append(Dirt(constants.DIRT_TOP))
        the_cast["dirt_top"][1].center_x = the_cast["dirt_top"][0].center_x + constants.MAX_X
        the_cast["dirt_top"][1].center_y = the_cast["dirt_top"][0].center_y
        the_cast["dirt_bottom"].append(Dirt(constants.DIRT_BOTTOM))
        the_cast["dirt_bottom"][1].center_x = the_cast["dirt_bottom"][0].center_x + constants.MAX_X
        the_cast["dirt_bottom"][1].center_y = the_cast["dirt_bottom"][0].center_y

        if Dirt.counter == 8:
            the_cast["FINISH_LINE"].append(Dirt(constants.FINISH_LINE))
            the_cast["FINISH_LINE"][0].center_y = constants.MAX_Y / 2
            the_cast["FINISH_LINE"][0].center_x = constants.MAX_X + 100

        if Dirt.counter > 10:
            arcade.close_window()
            
        self.finished = True
      

