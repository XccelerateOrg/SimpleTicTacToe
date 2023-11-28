# Simple Tic Tac Toe

The files are named as in the order of creation. I used O instead of zero is because you cannot import a name with numerical value (same as variable name).


O1_main: Always start with the main file which you will run. This is where you will write comments to ideate your app.

O2_game: The game board object is here. Although there is only one board at any point, it is still good to create a class out of it, because it provides us with an object to work with rather than a bunch of functions.

O3_Players: The player abstract class gives the players a structure. And we then create a HumanPlayer class extending the original class.


In the main file:

we create the play() which takes in the board, the two player objects, and let's them play.
This contains the main game logic.

In the main block, we create a sample game board, two human players, each with one symbol. And then call the play function for the actual game logic to run.



To run this program, simply run the O1_main.py file.

