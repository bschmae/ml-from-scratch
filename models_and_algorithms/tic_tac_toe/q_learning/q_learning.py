import sys
import os
import random
import copy

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(BASE_DIR)
from tic_tac_toe import utils

class QLearningAlgorithm():
    def __init__(self, ai_symbol, q_table={}):
        self.q_table = q_table
        self.gamma =  0.9 # discount factor
        self.alpha = 0.1  # learning rate
        self.epsilon = 1.0 # exploration rate
        self.min_epsilon = 0.1
        self.epsilon_decay_rate = 0.995
        self.ai_symbol = ai_symbol
        self.human_symbol = 'O' if ai_symbol == 'X' else 'X'

    def get_q_table(self):
        return self.q_table

    def get_ai_symbol(self):
        return self.ai_symbol

    def get(self, state, action):
        return self.q_table.get(state, {}).get(action, 0.0)

    def set(self, state, action, value):
        if state not in self.q_table:
            self.q_table[state] = {}
        self.q_table[state][tuple(action)] = value

    def temporal_difference(self, state, action, reward, next_state, legal_moves):
        old_q = self.get(state, tuple(action))
        future_q = [self.get(next_state, tuple(a)) for a in legal_moves]
        best_future_q = max(future_q) if future_q else 0

        new_q =  old_q + self.alpha * (reward + self.gamma *  best_future_q - old_q)
        self.set(state, action, new_q)

    def make_move(self, board):
        state = tuple(cell for row in board for cell in row)
        legal_moves = [[i, j] for i in range(3) for j in range(3) if board[i][j] == '']
        reward = 0
        board_copy = copy.deepcopy(board)

        # Exploration
        if random.random() < self.epsilon:
            action = random.choice(legal_moves)
            self.set(state, action, 0.0)
        # Exploitation
        else:
            q_values = {tuple(move): self.get(state, tuple(move)) for move in legal_moves}
            best_move = max(q_values, key=q_values.get)
            action = list(best_move)

        # Epsilon decay
        if self.epsilon > self.min_epsilon:
            self.epsilon *= self.epsilon_decay_rate

        # Apply move to board copy
        board_copy[action[0]][action[1]] = self.ai_symbol
        new_state = tuple(cell for row in board_copy for cell in row)

        # Check for win/draw in the new state
        win_object = utils.check_if_winner(board_copy)
        if win_object['isWinner']:
            reward = 1 if win_object['playerSymbol'] == self.ai_symbol else -1
        elif utils.check_if_draw(board_copy):
            reward = 0.5

        # Update Q-table
        next_legal_moves = [[i, j] for i in range(3) for j in range(3) if board_copy[i][j] == '']
        self.temporal_difference(state, action, reward, new_state, next_legal_moves)

        return f'{action[0] + 1} {action[1] + 1}'
