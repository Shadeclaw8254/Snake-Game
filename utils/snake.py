from utils.food import Food
from utils.scene import Scene
from utils.utils import directions
from utils.vector import Vector
from utils.game_object import GameObject
from utils.snake_part import SnakePart
from utils.game_over import GameOver
from utils.utils import WIDTH, HEIGHT
from utils.won import Won
import curses
import time

class Snake(GameObject):
    """
    A class representing the snake
    Of type GameObject
    """

    # Initializer
    def __init__(self):
        """
        :result: Returns nothing

        Initializes the Snake
        """

        # Set direction to right
        self.direction = directions[curses.KEY_RIGHT]
        # Set the body to an empty list
        self.body: list[SnakePart] = []

        # Loop from 0 to 2
        for i in range(0, 3):
            # Create a SnakePart
            part = SnakePart(Vector(i, 0))
            part.char = "—"
            # Append it to the body
            self.body.append(part)

    # A function that moves the snake
    def move(self):
        """
        :result: Returns nothing

        A function that moves the snake
        """

        # If the direction is left/right
        if self.direction in [Vector(1, 0), Vector(-1, 0)]:
            # Set the display character accordingly
            character = "—"

        # Otherwise, if the direction is up/down
        elif self.direction in [Vector(0, 1), Vector(0, -1)]:
            # Set the display character accordingly
            character = "|"

        # Pop the tail of the snake
        self.body.pop(0)

        # Create a new SnakePart and assign it to part
        part = SnakePart(
                Vector(
                    self.body[-1].x,
                    self.body[-1].y
                )
                +
                self.direction
        )

        # Assign the character of the part to the display character for rendering
        part.char = character # type: ignore

        # Append to body
        self.body.append(part)

    # Define a function to grow the snake
    def grow(self):
        """
        :result: Returns nothing

        A function that goes the snake
        """

        # If the direction is left/right
        if self.direction in [Vector(1, 0), Vector(-1, 0)]:
            # Set display character accordingly
            character = "—"

        # Otherwise, if the direction is up/down
        elif self.direction in [Vector(0, 1), Vector(0, -1)]:
            # Set display character accordingly
            character = "|"

        # Create a SnakePart and assign it to part
        part = SnakePart(
            Vector(
                self.body[-1].x,
                self.body[-1].y
            )
            +
            self.direction
        )

        # Set the part's char to the display character
        part.char = character # type: ignore

        # Append to body
        self.body.append(part)
    
    # Define a render function
    def render(self, buffer: list[list[str]]):
        """
        :buffer: A buffer to be rendered to
        :result: Returns nothing

        A function that renders the snake onto the buffer
        """

        # For each part of the body
        for i, body_part in enumerate(self.body):
            # If we see that it's the last character of the body
            if i == len(self.body) - 1:
                # We check the direction, and set the head character accordingly
                if self.direction == Vector(1, 0):
                    character = "→"

                elif self.direction == Vector(-1, 0):
                    character = "←"

                elif self.direction == Vector(0, 1):
                    character = "↓"

                elif self.direction == Vector(0, -1):
                    character = "↑"

            # Otherwise
            else:
                # Set the character to the default character to avoid errors.
                character = body_part.char

            # Finally, render the body part onto the buffer, with the chosen character.
            body_part.render(buffer, char=character) # type: ignore

    # Create a function that checks collision with a point
    def collides_with(self, point: Vector):
        """
        :point: The point to check collision against
        :result: Returns a boolean of whether the point collides with the snake

        Checks whether the snake collides with said point
        """

        # For each part of the body
        for part in self.body:
            # We check if it collides with the point
            if part.collides_with(point):
                # If so, return True
                return True
            
        # If nothing collided, return False.
        return False
    
    def has_player_won(self, width=WIDTH, height=HEIGHT):
        """
        :width: The screen's width
        :height: The screen's height
        :result: Returns a boolean of whether the player won

        Checks whether the player won
        """

        # If the player is the size of the screen
        if len(self.body) == width * height:
            # Return true
            return True
        
        # Otherwise, False
        return False

    # Define a physics_update function
    def physics_update(self, scene: Scene):
        """
        :scene: The scene from which to find the food

        Update the snake's position
        """

        # For each object in the scene
        for object in scene.get_objects():
            # We check if it's a Food object
            if type(object) == Food:
                # If so, assign it to food, then break the loop
                food = object
                # Set a flag
                food_found = True
                # Break
                break
        
        # If we didn't break
        else:
            # Set a flag to know there's no food
            food_found = False
        
        # Create a new head using the direction chosen by the player
        new_head = Vector(
            self.body[-1].x + self.direction.x,
            self.body[-1].y + self.direction.y
        )

        # If the new head isn't within the screen
        if (new_head.x > WIDTH - 1 or new_head.y > HEIGHT - 1 or
            new_head.x < 0 or new_head.y < 0):
            # Raise a GameOver error, because we hit the boundaries.
            raise GameOver(len(self.body))

        # For each part in the body
        for part in self.body:
            # Check if it collides with the new head
            if (new_head.x == part.x and
                new_head.y == part.y):
                # If it does, raise a GameOver error
                raise GameOver(len(self.body))
        
        # If we found food
        if food_found:
            # If it collides with the head
            if (new_head.x == food.x and # type: ignore
                new_head.y == food.y): # type: ignore
                # Grow
                self.grow()
                
                # If the player won, we raise Won()
                if self.has_player_won():
                    raise Won()

                # If the player didn't win, respawn the food
                food.respawn() # type: ignore
                # Then return
                return
        
        # If no food was hit, move the snake normally.
        self.move()
    
    # Define an input-handler
    def handle_input(self, stdscr: curses.window):
        """
        :stdscr: Window context

        Handles input for the snake
        """

        # Get the character, and put it into "character"
        character = stdscr.getch()

        # Create a vector representing the difference between the head and the part before it
        diff = Vector(
            self.body[-1].x - self.body[-2].x,
            self.body[-1].y - self.body[-2].y
        )

        # Check all possible characters, and set the direction accordingly.
        if character == curses.KEY_UP:
            direction = directions[curses.KEY_UP]

        elif character == curses.KEY_DOWN:
            direction = directions[curses.KEY_DOWN]

        elif character == curses.KEY_LEFT:
            direction = directions[curses.KEY_LEFT]

        elif character == curses.KEY_RIGHT:
            direction = directions[curses.KEY_RIGHT]

        # If impossible character
        else:
            # Return
            return
        
        # If the direction is valid
        if direction != -diff:
            # Set it as the snake's new direction
            self.direction = direction
