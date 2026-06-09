import random

from utils.game_object import GameObject
from utils.vector import Vector
from utils.scene import Scene
from utils.utils import WIDTH, HEIGHT

# Create a Food class
class Food(GameObject):
    """
    Food class
    """

    # Initializer
    def __init__(self, scene: Scene) -> None:
        """
        :result: Returns nothing

        Initializes the food
        """

        # Import the snake here, in order to not cause a loop, since Snake also imports Food
        from utils.snake import Snake
        
        # Set the food's character to "@"
        self.char = "@"

        # For each object in the scene
        for object in scene.get_objects():
            # Find the snake, and put it in self.snake.
            if type(object) == Snake:
                self.snake = object
                break
        
        # If we didn't break
        else:
            # Raise an exception
            raise Exception("Could not find a snake in the scene.")

        # Find a valid position for the food
        pos = self.choose_location()

        # Set the food's position to the found valid position
        self.x = pos.x
        self.y = pos.y
    
    # Create a function to choose a valid location
    def choose_location(self, screen_width=WIDTH, screen_height=HEIGHT):
        """
        :screen_width: The screen's width
        :screen_height: The screen's height
        :result: Returns a valid position to spawn the food

        A function to choose a random valid position on the screen
        """

        # Infinite loop
        while True:
            # Randomize position
            position = Vector(
                random.randint(0, screen_width - 1),
                random.randint(0, screen_height - 1)
            )

            # If the position is valid
            if not self.snake.collides_with(position):
                # Break
                break
        
        # Return the found valid position
        return position

    # Create a function to respawn the food
    def respawn(self, screen_width=20, screen_height=10):
        """
        :screen_width: The screen's width
        :screen_height: The screen's height
        :result: Returns nothing

        A function to respawn the food in another valid position
        """

        # Find a new valid position
        pos = self.choose_location()

        # Put it as the food's new position
        self.x = pos.x
        self.y = pos.y

    # Create a function to render the food
    def render(self, buffer: list[list[str]]):
        """
        :buffer: The buffer to render the food onto
        :result: Returns nothing

        Renders the food onto the buffer
        """

        # Set the food's location in the buffer to the food's display character
        buffer[self.y][self.x] = self.char