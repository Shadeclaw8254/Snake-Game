import random

from utils.game_object import GameObject
from utils.vector import Vector
from utils.scene import Scene
from utils.utils import WIDTH, HEIGHT

class Food(GameObject):
    def __init__(self, scene: Scene) -> None:
        from utils.snake import Snake
        
        self.char = "@"

        for object in scene.get_objects():
            if type(object) == Snake:
                self.snake = object
                break
            
        else:
            raise Exception("Could not find a snake in the scene.")

        pos = self.choose_location()

        self.x = pos.x
        self.y = pos.y

    def choose_location(self, screen_width=WIDTH, screen_height=HEIGHT):
        while True:
            position = Vector(
                random.randint(0, screen_width - 1),
                random.randint(0, screen_height - 1)
            )

            if not self.snake.collides_with(position):
                break

        return position

    def respawn(self, screen_width=20, screen_height=10):
        pos = self.choose_location()
        self.x = pos.x
        self.y = pos.y

    def render(self, buffer: list[list[str]], **kwargs):
        buffer[self.y][self.x] = self.char