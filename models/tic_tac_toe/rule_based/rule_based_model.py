from tic_tac_toe import utils
import random 

CORNERS = [[0, 0], [0, 2], [2, 0], [2, 2]]
EDGES = [[0, 1], [1, 0], [2, 1], [1, 2]]

class RuleBasedAI:
    def __init__(self, ai_symbol, opponent_symbol):
        self.is_ai_turn = False
        self.ai_symbol = ai_symbol
        self.opponent_symbol = opponent_symbol

    def get_ai_symbol(self):
        return self.ai_symbol

    def make_move(self, board):
        # Priority order

        try:
            # 1. Check if AI can win
            for i, row in enumerate(board):
                for j, cell in enumerate(row):
                    if cell ==  '':
                        board[i][j] = self.ai_symbol

                        if utils.check_if_winner(board)['isWinner']:
                            board[i][j] = ''
                            return f'{i + 1} {j + 1}'

                        board[i][j] = ''

            # 2. Check if AI can block opponent's win
            for i, row in enumerate(board):
                for j, cell in enumerate(row):
                    if cell ==  '':
                        board[i][j] = self.opponent_symbol

                        if utils.check_if_winner(board)['isWinner']:
                            board[i][j] = ''
                            return f'{i + 1} {j + 1}'

                        board[i][j] = ''

            # 3. Take center if available
            # Doing this 50% of the time just to mix things up
            if random.choice([True, False]):
                if board[1][1] == '':
                    return '2 2'

            # 4. Take a corner
            for r, c in CORNERS:
                if board[r][c] == '':
                    return f'{r + 1} {c + 1}'

            # 5. Take an edge
            for r, c in EDGES:
                if board[r][c] == '':
                    return f'{r + 1} {c + 1}'

        except Exception as e:
            raise RuntimeError("Error in AI move logic") from e
