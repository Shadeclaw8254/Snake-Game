class GameOver(Exception):
    def __init__(self, score):
        self.score = score