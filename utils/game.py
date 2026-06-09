import curses
from utils.scene import Scene
from utils.snake import Snake
from utils.food import Food
from utils.game_over import GameOver
from utils.utils import WIDTH, HEIGHT

class Game:
    def __init__(self, width=WIDTH, height=HEIGHT) -> None:
        self.WIDTH = width
        self.HEIGHT = height

        self.buffer = [
            ["#"] * self.WIDTH
            for _ in range(self.HEIGHT)
        ]

        self.scene = Scene()

        self.running = True

        self.frames_passed = 0

    def render(self, stdscr: curses.window) -> None:
        for object in self.scene.get_objects():
            object.render(self.buffer)

        for y, row in enumerate(self.buffer):
            for x, col in enumerate(row):
                stdscr.addch(y, x, col, curses.color_pair(1))

        stdscr.refresh()
    
    def handle_input(self, stdscr: curses.window):
        for object in self.scene.get_objects():
            object.handle_input(stdscr)
    
    def set_pixel(self, x, y, ch: str):
        self.buffer[y][x] = ch

    def clear(self):
        for y, row in enumerate(self.buffer):
            for x, _ in enumerate(row):
                self.set_pixel(x, y, " ")

    def run(self, stdscr: curses.window):
        stdscr.nodelay(True)
        curses.curs_set(0)
        curses.start_color()
        curses.use_default_colors()

        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        self.snake = Snake()
        self.scene.add_object(self.snake)

        self.food = Food(self.scene)
        self.scene.add_object(self.food)

        # Game loop
        while self.running:
            self.update(stdscr)

        return f"Game Over! You scored {self.score}!"

    def update(self, stdscr):
        # Clear screen
        self.clear()

        if self.frames_passed % 2000 == 0:
            self.physics_update()

        self.handle_input(stdscr)

        self.render(stdscr)

        self.frames_passed += 1

    def physics_update(self):
        for object in self.scene.get_objects():
            try:
                object.physics_update(self.scene)
            except GameOver as e:
                self.running = False
                self.score = e.score