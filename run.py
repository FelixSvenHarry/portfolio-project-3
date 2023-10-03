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

    def get_ship_location(self):
        """
        Handels the players input for ship row and column location
        as well as catching potential errors when inputs are being made.
        """
        row = input('Enter a ship row 1-8: ').upper()
        while row not in '12345678':
            print("Invalid integer, please enter a valid row ")
            row = input('Enter a ship row 1-8: ')
        column = input('Enter a ship column A-H: ').upper()
        while column not in 'ABCDEFGH':
            print("Invalid value, please enter a valid column ")
            column = input('Enter a ship column A-H: ')
        return int(row) - 1, ord(column) - ord('A')
    
    