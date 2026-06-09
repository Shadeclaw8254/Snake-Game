import curses
from utils.vector import Vector

directions = {
    curses.KEY_RIGHT: Vector(1, 0),
    curses.KEY_LEFT: Vector(-1, 0),
    curses.KEY_UP: Vector(0, -1),
    curses.KEY_DOWN: Vector(0, 1)
}

WIDTH = 20
HEIGHT = 10

def log(log: str):
    with open("log.txt", "a") as f:
        f.write(log)