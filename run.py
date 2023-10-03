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

    def print_board(self):
        """
        Prints the game board, with rows labeled
        1 to 8 and columns labeled "A" to "H".
        """
        print(' A B C D E F G H')
        print(' ***************')
        row_num = 1
        for guess_row in self.guess_pattern:
            print("%d|%s|" % (row_num, "|".join(guess_row)))
            row_num += 1
    
    

