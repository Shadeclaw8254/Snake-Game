import curses
from utils.game import Game

if __name__ == "__main__":
    game = Game()
    message = curses.wrapper(game.run)
    print(message)