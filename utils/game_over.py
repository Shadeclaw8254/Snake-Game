class GameOver(Exception):
    """
    A special exception for when you lose
    """

    def __init__(self, score):
        """
        :score: The score you got in the game
        :result: Returns nothing
        """

        # Set score to the score
        self.score = score