from abc import ABC, abstractmethod
from O2_game import Game


class Player(ABC):
    @abstractmethod
    def get_move(self, game: Game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__()
        self.letter = letter

    def get_move(self, game: Game):
        valid_square = False
        while not valid_square:
            square = input(f"{self.letter}\'s turn. Input a move (1-9): ")
            try:
                square = int(square)
                if game.make_move(square, self.letter):
                    valid_square = True
                else:
                    print("Invalid move!")
            except ValueError:
                pass
        return True


