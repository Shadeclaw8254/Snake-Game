import curses

class GameObject:
    """
    Anything that exists in the game (the top node)
    """

    def render(self, buffer: list[list[str]]): """An overridable function to render the game object"""
    def handle_input(self, stdscr: curses.window): """An overridable function to handle inputs"""
    def physics_update(self, scene): """An overridable function to update the game object's attributes"""