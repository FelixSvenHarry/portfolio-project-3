from random import randint

class Board:
    def __init__(self, size=8):
        """
        Creates the game board grid with the given size, 
        default 8 by 8.
        """
        self.size = size
        self.hidden_pattern = [[' ']*size for _ in range(size)]
        self.guess_pattern = [[' ']*size for _ in range(size)]