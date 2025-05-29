class TicTacToe:
    def __init__(self):
        self.board = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
        self.player_x = 'X'
        self.player_o = 'O'
        self.player_turn = 'X'


    def print_board(self):
        for _ in self.board:
            print(_)


    def update_board(self, move):
        row, col = map(lambda x: int(x) - 1, move.split())
        self.board[row][col] = self.player_turn


    def get_player_input(self):
        print(f'Player {self.player_turn}, enter your move (row and column):')

        move = input('>> ').strip()

        return move


    def check_if_valid_move(self, move):
        valid_entries = ['1', '2', '3']
        parts = move.split()

        for part in parts:
            if part not in valid_entries:
                print('Must enter a number between 1-3 for row and column')
                return False

        if len(parts) != 2:
            print('Must select a row and column!')
            return False

        row, col = map(lambda x: int(x) - 1, parts)

        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print('Invalid cell selection! Pick a number between 1 and 3.')
            return False

        position = self.board[row][col]

        if position != '':
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

    def check_if_winner(self):
        # Check horizontally
        for row in self.board:
            if row[0] != '' and row[0] == row[1] == row[2]:
                return True

        # Check vertically
        for col in range(3):
            if self.board[0][col] != '' and \
                self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return True

        # Check diagonally
        center = self.board[1][1]
        if center != '':
            if center == self.board[0][0] == self.board[2][2]:
                return True
            if center == self.board[2][0] == self.board[0][2]:
                return True

        return False


    def play_game(self):
        print('Player O goes first.')

        while True:
            self.print_board()

            move = self.get_player_input()
            valid_move = self.check_if_valid_move(move)

            while not valid_move:
                move = self.get_player_input()
                if self.check_if_valid_move(move):
                    break

            self.update_board(move)

            is_draw = self.check_if_draw()
            if is_draw:
                self.print_board()
                print('The game is a draw!')
                return

            is_winner = self.check_if_winner()
            if is_winner:
                self.print_board()
                print(f'Player {self.player_turn} wins!')
                return

            self.update_player_turn()

