import curses
from utils.game_object import GameObject
from utils.vector import Vector

class SnakePart(GameObject):
    def __init__(self, pos: Vector) -> None:
        self.char = "#"
        self.x = pos.x
        self.y = pos.y

    def render(self, buffer: list[list[str]], **kwargs):
        if "char" in kwargs:
            buffer[self.y][self.x] = kwargs["char"]

        else:
            buffer[self.y][self.x] = self.char

    def collides_with(self, point: Vector):
        if self.x == point.x and self.y == point.y:
            return True
        
        return False