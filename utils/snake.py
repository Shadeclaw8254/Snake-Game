from utils.food import Food
from utils.scene import Scene
from utils.utils import directions
from utils.vector import Vector
from utils.game_object import GameObject
from utils.snake_part import SnakePart
from utils.game_over import GameOver
from utils.utils import WIDTH, HEIGHT
import curses
import time

class Snake(GameObject):
    def __init__(self):
        self.direction = directions[curses.KEY_RIGHT]
        self.body: list[SnakePart] = []

        for i in range(0, 3):
            part = SnakePart(Vector(i, 0))
            part.char = "—"
            self.body.append(part)

    def move(self):
        if self.direction in [Vector(1, 0), Vector(-1, 0)]:
            character = "—"

        elif self.direction in [Vector(0, 1), Vector(0, -1)]:
            character = "|"

        self.body.pop(0)

        part = SnakePart(
                Vector(
                    self.body[-1].x,
                    self.body[-1].y
                )
                +
                self.direction
        )

        part.char = character # type: ignore

        self.body.append(part)

    def grow(self):
        if self.direction in [Vector(1, 0), Vector(-1, 0)]:
            character = "—"

        elif self.direction in [Vector(0, 1), Vector(0, -1)]:
            character = "|"

        
        part = SnakePart(
            Vector(
                self.body[-1].x,
                self.body[-1].y
            )
            +
            self.direction
        )

        part.char = character # type: ignore

        self.body.append(part)

    def render(self, buffer: list[list[str]]):
        for i, body_part in enumerate(self.body):
            if i == len(self.body) - 1:
                if self.direction == Vector(1, 0):
                    character = "→"

                elif self.direction == Vector(-1, 0):
                    character = "←"

                elif self.direction == Vector(0, 1):
                    character = "↓"

                elif self.direction == Vector(0, -1):
                    character = "↑"

            else:
                character = body_part.char

            body_part.render(buffer, char=character) # type: ignore

    def collides_with(self, point: Vector):
        for part in self.body:
            if part.collides_with(point):
                return True
            
        return False
    
    def physics_update(self, scene: Scene):
        for object in scene.get_objects():
            if type(object) == Food:
                food = object
                break

        else:
            self.move()

            return
        
        new_head = Vector(
            self.body[-1].x + self.direction.x,
            self.body[-1].y + self.direction.y
        )
        
        if (new_head.x > WIDTH - 1 or new_head.y > HEIGHT - 1 or
            new_head.x < 0 or new_head.y < 0):
            raise GameOver(len(self.body))

        for part in self.body:
            if (new_head.x == part.x and
                new_head.y == part.y):
                raise GameOver(len(self.body))

        if (new_head.x == food.x and
            new_head.y == food.y):
            self.grow()
            food.respawn()
            return
        
        self.move()

    def handle_input(self, stdscr: curses.window):
        character = stdscr.getch()

        diff = Vector(
            self.body[-1].x - self.body[-2].x,
            self.body[-1].y - self.body[-2].y
        )

        if character == curses.KEY_UP:
            direction = directions[curses.KEY_UP]

        elif character == curses.KEY_DOWN:
            direction = directions[curses.KEY_DOWN]

        elif character == curses.KEY_LEFT:
            direction = directions[curses.KEY_LEFT]

        elif character == curses.KEY_RIGHT:
            direction = directions[curses.KEY_RIGHT]

        else:
            return
        
        if direction != -diff:
            self.direction = direction
