import os
from pathlib import Path
DIR = Path(__file__).resolve().parent
DIRROOT = DIR.resolve().parent

MAX_X = 800
MAX_Y = 600


CAR_X = 25

CAR_MOVE_SCALE = 10
OBSTACLE_INTERVAL = 200
DIRT_TOP = DIRROOT.joinpath("images/dirt_top.png")
DIRT_BOTTOM = DIRROOT.joinpath("images/dirt_bottom.png")
OBSTACLE_ONE = DIRROOT.joinpath("images/barrier.png")
FINISH_LINE = DIRROOT.joinpath("images/finish-line.png")
OBSTACLES_LIST = []
OBSTACLES_LIST.append(DIRROOT.joinpath("images/barrier.png"))

GAME_TITLE = "RIP PAUL WALKER"
CAR_IMAGE = DIRROOT.joinpath("images/racecar.png")
