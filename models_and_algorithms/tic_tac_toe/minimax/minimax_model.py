from tic_tac_toe import utils
import copy

class MinimaxModel():
    def __init__(self, ai_symbol):
        self.ai_symbol = ai_symbol
        self.human_symbol = 'O' if ai_symbol == 'X' else 'X'

    def get_ai_symbol(self):
        return self.ai_symbol

    def make_move(self, board):
        minimax_obj = self.minimax(board, True)
        return minimax_obj['bestMove']

    def minimax(self, board, is_maximizing):
        best_score = float('-inf') if is_maximizing else float('inf')
        best_move = ''
        legal_moves = []
        win_object = utils.check_if_winner(board)

        if win_object['isWinner']:
            if win_object['playerSymbol'] == self.ai_symbol:
                return { 'bestScore': 1, 'bestMove': None }
            if win_object['playerSymbol'] == self.human_symbol:
                return { 'bestScore': -1, 'bestMove': None }

        if utils.check_if_draw(board):
            return { 'bestScore': 0, 'bestMove': None }

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == '':
                    legal_moves.append([i, j])

        for move in legal_moves:
            board_copy = copy.deepcopy(board)
            player_symbol = self.ai_symbol if is_maximizing else self.human_symbol

            board_copy[move[0]][move[1]] = player_symbol

            child_score = self.minimax(board_copy, not is_maximizing)['bestScore']

            if is_maximizing:
                if child_score > best_score:
                    best_score = child_score
                    best_move = f'{move[0] + 1} {move[1] + 1}'
            else:
                if child_score < best_score:
                    best_score = child_score
                    best_move = f'{move[0] + 1} {move[1] + 1}'

        return {
            'bestScore': best_score,
            'bestMove': best_move
            }
