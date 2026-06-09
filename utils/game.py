import curses
from utils.scene import Scene
from utils.snake import Snake
from utils.food import Food
from utils.game_over import GameOver
from utils.utils import WIDTH, HEIGHT
from utils.won import Won

# Create class Game
class Game:
    """
    A game class
    """

    # Define an initialization function
    def __init__(self, width=WIDTH, height=HEIGHT) -> None:
        """
        :width: The width of the screen
        :height: The height of the screen
        :result: Returns nothing

        And initializer that sets everything up for the game.
        """
        # Inside of it, we define the width and height.
        self.width = width
        self.height = height

        # We create a buffer to store characters.
        self.buffer = [
            ["#"] * self.width
            for _ in range(self.height)
        ]

        # Then, we create a new Scene.
        self.scene = Scene()

        # Set a flag to know whether the game should keep running.
        self.running = True

        # Set a flag for whether the player won or lost (false = lost, true = won)
        self.end_state = False

        # Counts the amount of frames passed.
        self.frames_passed = 0

    # Define a render function that renders the whole game.
    def render(self, stdscr: curses.window) -> None:
        """
        :stdscr: The window context
        :result: Returns nothing

        Renders the whole game onto the terminal
        """

        # For each object in the scene,
        for object in self.scene.get_objects():
            # call the object's render function.
            object.render(self.buffer)

        # For each row in the buffer
        for y, row in enumerate(self.buffer):
            # We get the character at each column of the row
            for x, col in enumerate(row):
                # To finally print it out using Curses.
                stdscr.addch(y, x, col, curses.color_pair(1))

        # Refresh the screen to see the new buffer.
        stdscr.refresh()
    
    # Define a function to handle the game's input.
    def handle_input(self, stdscr: curses.window):
        """
        :stdscr: Window context
        :result: Returns nothing
        
        Allows every object in the game to handle its input
        """
        # For each object in the scene
        for object in self.scene.get_objects():
            # Call its input-handling function.
            object.handle_input(stdscr)
    
    # Define a function for placing characters on the screen.
    def set_pixel(self, x, y, ch: str):
        """
        :x: X position on the screen
        :y: Y position on the screen
        :ch: A string of length 1 that will be rendered at (x,y)
        :result: Returns nothing

        Renders a character "ch" at position (x,y)
        """
        # Simply replace the character at the location in the buffer with the new character.
        self.buffer[y][x] = ch

    # Define a function to clear the screen for the next render.
    def clear(self):
        """
        :result: Returns nothing

        A function that clears the screen
        """

        # For each row,
        for y, row in enumerate(self.buffer):
            # And column,
            for x, _ in enumerate(row):
                # Replace it with a space character.
                self.set_pixel(x, y, " ")

    # Define the entry point of the program
    def run(self, stdscr: curses.window):
        """
        :stdscr: Window context
        :result: Returns nothing

        Runs the game
        """
        # Set it up so that getch() doesn't hang when you don't press anything
        stdscr.nodelay(True)

        # Make the cursor invisible
        curses.curs_set(0)

        # Set it up so you can write characters with colors
        curses.start_color()

        # Set the palette to the default terminal colors
        curses.use_default_colors()

        # Initiate a color pair of which the background color is white, and the foreground is black.
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        # Define the snake.
        self.snake = Snake()

        # Add the snake to the scene
        self.scene.add_object(self.snake)

        # Define the food
        self.food = Food(self.scene)

        # Add the food to the scene
        self.scene.add_object(self.food)

        # Game loop
        while self.running:
            # Update everything
            self.update(stdscr)

        # At the end
        # If we won
        if self.end_state:
            # We return a message saying the player won the game.
            return f"You won!"
        
        # Otherwise, if we lost
        else:
            # We return a game over message, with a score.
            return f"Game Over! You scored {self.score}!"

    # Define an update function
    def update(self, stdscr):
        """
        :stdscr: Window context
        :result: Returns nothing

        Updates everything
        """

        # Clear screen
        self.clear()

        # Every 2000 frames, we update the game.
        if self.frames_passed % 5000 == 0:
            self.physics_update()

        # We handle input separately, so it's not all choppy and annoying.
        self.handle_input(stdscr)

        # We render the scene.
        self.render(stdscr)

        # Add one frame to the frames passed, to know that we finished rendering 1 frame.
        self.frames_passed += 1
    
    # Define a physics update function
    def physics_update(self):
        """
        :result: Returns nothing

        A function that updates positions
        """

        # For each object in the scene
        for object in self.scene.get_objects():
            try:
                # Try to call its physics_update function
                object.physics_update(self.scene)
            except GameOver as e:
                # If we encounter a GameOver error
                # We stop the game, set the score to the actual score, and set the end_state to False.
                self.running = False
                self.score = e.score
                self.end_state = False
            except Won as e:
                # Otherwise, if we encounter a Won error
                # Set running to False and end_state to True
                self.running = False
                self.end_state = True