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
            row = input('Enter a ship row 1-8:\n')
        column = input('Enter a ship column A-H: ').upper()
        while column not in 'ABCDEFGH':
            print("Invalid value, please enter a valid column ")
            column = input('Enter a ship column A-H:\n')
        return int(row) - 1, ord(column) - ord('A')

    def create_ships(self):
        """
        Creates 5 ships randomly on the
        hidden game board.
        """
        for ship in range(5):
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
            while self.hidden_pattern[ship_r][ship_cl] == 'X':
                ship_r, ship_cl = randint(0, 7), randint(0, 7)
            self.hidden_pattern[ship_r][ship_cl] = 'X'

    def count_hit_ships(self):
        """
        Counts the number of hit ships on the
        guess pattern board and returns the value.
        """
        count = 0
        for row in self.guess_pattern:
            for column in row:
                if column == 'X':
                    count += 1
        return count

    def play_game(self, turns=10):
        """
        Manages the gameplay loop, allowing the player 
        to make guesses and tracking the game's progress.
        """
        self.create_ships()
        while turns > 0:
            print('Welcome to Battleships!')
            self.print_board()
            row, column = self.get_ship_location()
            if self.guess_pattern[row][column] == '-':
                print(' You already guessed that,\n please choose a new location ')
            elif self.guess_pattern[row][column] == 'X':
                print(' You already guessed that,\n please choose a new location ')
            elif self.hidden_pattern[row][column] == 'X':
                print(' Congratulations you have hit the battleship! ')
                self.guess_pattern[row][column] = 'X'
                turns -= 1
            else:
                print('Haha, You missed my ship! Try again!')
                self.guess_pattern[row][column] = '-'
                turns -= 1
            if self.count_hit_ships() == 5:
                print("Congratulations you have sunk all my battleships, great work! ")
                break
            print(' You have ' + str(turns) + ' turns remaining ')
            if turns == 0:
                print('Game Over ')

def main():
    battleship_board = Board()
    battleship_board.play_game()

main()