from O2_game import Game, print_board_nums
from O3_Players import HumanPlayer


def play(game: Game, player1: HumanPlayer, player2: HumanPlayer):
    symbol_to_play = player1.letter
    print_board_nums()
    while game.num_empty_squares() > 0:
        if symbol_to_play == game.cross_symbol:
            _ = player1.get_move(game=game)
        else:
            _ = player2.get_move(game=game)
        print(game)
        if game.check_winner():
            print(f"{game.get_winner()} WON!")
            break
        symbol_to_play = game.naught_symbol if symbol_to_play == game.cross_symbol else game.cross_symbol


if __name__ == '__main__':
    # I need a game class
    sample_game = Game()
    # I need player classes
    player_1 = HumanPlayer(sample_game.cross_symbol)
    player_2 = HumanPlayer(sample_game.naught_symbol)
    # I need a play function
    play(sample_game, player_1, player_2)
