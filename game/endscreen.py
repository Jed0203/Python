import arcade
from game import constants

class End_Menu(arcade.View):

    def __init__(self, view):
        super().__init__()
        self.view = view
    
    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.GREEN)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, constants.MAX_X - 1, 0, constants.MAX_Y - 1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text(constants.GAME_TITLE, constants.MAX_X / 2, constants.MAX_Y / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Finish! Final time was: ", constants.MAX_X / 2, constants.MAX_Y / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        quit()
        """ If the user presses the mouse button, end the game. """
        


    
