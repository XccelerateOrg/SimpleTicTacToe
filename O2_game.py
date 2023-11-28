class Game:
    def __init__(self):
        self.game_board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.blank = -1
        self.cross = 0
        self.naught = 1
        self.winner = None
        self.cross_symbol = 'x'
        self.naught_symbol = 'o'

    def __str__(self):
        disp_board = ""
        for i in range(3):
            for j in range(3):
                if self.game_board[i][j] == self.blank:
                    disp_board += " |"
                elif self.game_board[i][j] == self.cross:
                    disp_board += "x|"
                else:
                    disp_board += "o|"
            disp_board = disp_board[:-1] + "\n"
        return disp_board

    def available_moves(self):
        available_ids = [(i * 3) + (j + 1) for i in range(3) for j in range(3) if self.game_board[i][j] == -1]
        return available_ids

    def num_empty_squares(self):
        return len(self.available_moves())

    def make_move(self, square, letter):
        i, j = (square - 1) // 3, (square - 1) % 3
        if self.game_board[i][j] == self.blank:
            if letter == self.cross_symbol:
                self.game_board[i][j] = self.cross
                if self.check_winning_move(i, j):
                    self.winner = self.cross_symbol
            else:
                self.game_board[i][j] = self.naught
                if self.check_winning_move(i, j):
                    self.winner = self.naught_symbol
            return True
        else:
            return False

    def check_winning_move(self, row, col):
        if all([self.game_board[row][j] == self.game_board[row][col] for j in range(3)]):
            return True
        if all([self.game_board[i][col] == self.game_board[row][col] for i in range(3)]):
            return True
        if [row, col] in [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]:
            # check main diagonal
            if all([self.game_board[i][i] == self.game_board[row][col] for i in range(3)]):
                return True
            # check the secondary diagonal
            elif all([self.game_board[i][j] == self.game_board[row][col] for i, j in [[0, 2], [1, 1], [2, 0]]]):
                return True
        return False

    def check_winner(self):
        return True if self.winner else False

    def get_winner(self):
        return self.winner

    def reset_move(self, square):
        # This function is required when we will implement AI to play with us
        i, j = (square - 1) // 3, (square - 1) % 3
        self.game_board[i][j] = self.blank
        self.winner = None


def print_board_nums():
    # This function is needed to show the game board at the beginning
    number_board = list(range(1, 10))
    for i in range(3):
        for j in range(3):
            print(f"|{number_board[(i * 3) + j]}|", end='')
        print('\n', '-' * 7)
