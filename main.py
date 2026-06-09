from __future__ import annotations
import curses
from utils.game import Game

if __name__ == "__main__":
    game = Game() # Define the game
    message = curses.wrapper(game.run) # Run it with Curses (Curses is a terminal UI renderer)
    print(message) # At the end of the game, print the returned message.
