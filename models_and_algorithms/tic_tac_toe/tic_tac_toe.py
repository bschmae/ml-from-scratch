import utils as utils
import time
import random

class TicTacToe:
    def __init__(self):
        self.board = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
        self.player_x = 'X'
        self.player_o = 'O'
        self.player_turn = 'O'
        self.training_flag = False

    def print_board(self):
        for _ in self.board:
            print(_)

    def update_board(self, move):
        row, col = map(lambda x: int(x) - 1, move.split())
        self.board[row][col] = self.player_turn

    def get_player_input(self):
        if not self.training_flag:
            print(f'Player {self.player_turn}, enter your move (row and column):')

        move = input('>> ').strip()

        return move

    def check_if_valid_move(self, move):
        valid_entries = ['1', '2', '3']

        if move is None:
            return False
        parts = move.split()

        for part in parts:
            if part not in valid_entries:
                if not self.training_flag:
                    print('Must enter a number between 1-3 for row and column', parts)
                return False

        if len(parts) != 2:
            if not self.training_flag:
                print('Must select a row and column!')
            return False

        row, col = map(lambda x: int(x) - 1, parts)

        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            if not self.training_flag:
                print('Invalid cell selection! Pick a number between 1 and 3.')
            return False

        position = self.board[row][col]

        if position != '':
            if not self.training_flag:
                print('The square you chose is already occupied.')
                print('Please choose a new position!')
            return False

        return True

    def update_player_turn(self):
        if self.player_turn == self.player_x:
            self.player_turn = self.player_o
        else:
            self.player_turn = self.player_x

    def check_if_draw(self):
        board = self.board

        is_draw = True

        for row in board:
            for col in row:
                if col == '':
                    is_draw = False
                    break

        return is_draw

    def get_player_move(self, ai_1, ai_2):
        move = None

        # ai vs ai
        if ai_2 is not None:
            if ai_1.get_ai_symbol() == self.player_turn:
                move = ai_1.make_move(board=self.board)
            else:
                move = ai_2.make_move(board=self.board)
        else:
            if self.player_turn == ai_1.get_ai_symbol():
                if not self.training_flag:
                    print(f'Player {ai_1.get_ai_symbol()} is thinking...')
                num = random.uniform(1, 3)
                time.sleep(num)
                move = ai_1.make_move(board=self.board)
            else:
                move = self.get_player_input()

        return move

    def play_game(self, ai_1, ai_2, training_flag=False):
        self.training_flag = training_flag
        if not training_flag:
            print('Player O goes first.')

        while True:
            if not training_flag:
                self.print_board()
                print('------------')

            move = self.get_player_move(ai_1, ai_2)
            valid_move = self.check_if_valid_move(move)

            while not valid_move:
                move = self.get_player_move(ai_1, ai_2)
                if self.check_if_valid_move(move):
                    break

            self.update_board(move)

            is_draw = self.check_if_draw()
            if is_draw:
                if not training_flag:
                    self.print_board()
                    print('The game is a draw!')
                return

            is_winner = utils.check_if_winner(self.board)['isWinner']
            if is_winner:
                if not training_flag:
                    self.print_board()
                    print(f'Player {self.player_turn} wins!')
                return self.player_turn

            self.update_player_turn()
