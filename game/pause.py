import arcade
import time
from game import constants

class Pause_Menu(arcade.View):

    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_draw(self):
        arcade.set_background_color(arcade.csscolor.ROYAL_BLUE)
        arcade.set_viewport(0, constants.MAX_X - 1, 0, constants.MAX_Y - 1)

    def on_show(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("Game Paused", constants.MAX_X / 2, constants.MAX_Y / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", constants.MAX_X / 2, constants.MAX_Y / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        self.window.show_view(self.game_view)
        arcade.set_background_color(arcade.color.BLACK)
        
        self.start_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        arcade.play_sound(self.start_sound)
        