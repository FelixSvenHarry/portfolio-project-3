# BATTLESHIPS
Battleships is a fun and casual game played through the terminal which runs on Code Institute's mock terminal through heroku.

[try the game out here!](https://pp3-battleships-felix-5ce17c512714.herokuapp.com/)
![Battleships](/assets/images/battleships.png)

## HOW TO PLAY
When you start the game you're faced with an 8 by 8 grid, where the columns are listed by letters from 'A' to 'H' and the rows listed as numbers from 1 to 8.

you are then promted to input which row you wish to play on by chooshing a number between 1 and 8 and the asked to pick which column you wish to check by picking a letter between 'A' and 'H'.

Successful hits are makrked with an 'X' as well as a message declaring you've successfully sunka ship.

misses are shown as '-' as well as a messages saying that you've missed and to please try again.

if you within 10 turns manage to sink all four ships the computer has hid you win.

## EXISTING FEATURES

- Random board generation
    - The ships are randomly generated on the board each game in order for increased replayability.
    - The computers ships are hidden from the player.

![play game](/assets/images/play-game.png)

- Input validation
    - The game checks that the value being input corresponds to a valid move.
    - you can't enter the same guess two times in a row.
    - you can't hit the same ship twice.

![error checking](/assets/images/error-checking.png)

## FEATURES TO IMPLEMENT
- Pick the size of the board.
- The ability to pick how many ships should be on the board.
- The ability pick diffrently sized ships.
- The ability to play against another player.

## DATA MODEL

I chose to use a Board calss model. The game generates the board class wich creates the main plaing filed.

The board class stores all vital information such as the board size, the ships locations, the guesses made as well as number of turns left.

## TESTING

Ive tested the game in the following ways.
- Run the code through the PEP8 code validator to make sure there is no problems with my code.
- Fed the game invalid inputs to make sure no invalid inputs are able to be made.
- Tested the game in my local terminal, in VScode as well as in the Code Institute Heroku terminal.

## REMAINING BUGS

- No bugs remaining.

## VALIDATOR TESTING

- PEP8
    - No bugs were found.

## DEPLOYMENT
- This game was deployed using Code Institutes mock terminal through Heroku.
    - fork or clone this repository.
    - Create a Heroku app.
    - Set the buildbacks to 'Python' and 'Nodejs'.
    - Link the Heroku app to the repository.
    - Klick the deploy button.

## CREDITS

- Code Institute for providing the template as well as the mock terminal.
- [copyassignment](https://copyassignment.com/battleship-game-code-in-python/) for providing pointers on details for the battleships game.
