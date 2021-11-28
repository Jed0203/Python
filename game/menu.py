import arcade
from game import constants

class Main_Menu(arcade.View):
    def set_parameter(self, cast, script, input_service):
        self._cast = cast
        self._script = script
        self._input_service = input_service
    
    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.ROYAL_BLUE)
        arcade.set_viewport(0, constants.MAX_X - 1, 0, constants.MAX_Y - 1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text(constants.GAME_TITLE, constants.MAX_X / 2, constants.MAX_Y / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", constants.MAX_X / 2, constants.MAX_Y / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        from game.director import Director
        game_view = Director(self._cast, self._script, self._input_service)
        game_view.setup()
        self.window.show_view(game_view)
        self.start_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        arcade.play_sound(self.start_sound)