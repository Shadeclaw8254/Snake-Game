import curses
from utils.game_object import GameObject
from utils.vector import Vector

class SnakePart(GameObject):
    """
    A class representing snake parts
    Is a GameObject
    """

    # An initializer
    def __init__(self, pos: Vector) -> None:
        """
        :pos: The position of the snake part
        :result: Returns nothing

        Initializes the SnakePart
        """

        # Set the character as "#" (default in case not handled outside the object)
        self.char = "#"
        # Set the position of the SnakePart
        self.x = pos.x
        self.y = pos.y

    # Create a render function
    def render(self, buffer: list[list[str]], **kwargs):
        """
        :buffer: A buffer to be rendered onto
        :result: Returns nothing

        A function that renders the SnakePart
        """

        # If we got a character fed into the renderer
        if "char" in kwargs:
            # Blit that character
            buffer[self.y][self.x] = kwargs["char"]

        # Otherwise
        else:
            # Set it to the default character
            buffer[self.y][self.x] = self.char
    
    # Create a function that detects collision with a point
    def collides_with(self, point: Vector) -> bool:
        """
        :point: The point to be checked against
        :result: A boolean of whether collision was found

        Checks collision against a point
        """

        # If both x and y match for both self and the point
        if self.x == point.x and self.y == point.y:
            # Return true
            return True
        
        # Otherwise, false
        return False