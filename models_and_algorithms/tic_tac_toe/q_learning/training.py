import os
import sys
import pickle

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(BASE_DIR)
from tic_tac_toe import TicTacToe

import random

class RandomAI:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_ai_symbol(self):
        return self.symbol

    def make_move(self, board):
        # Find all legal moves (empty cells)
        legal_moves = [
            [i, j] for i in range(3)
            for j in range(3) if board[i][j] == ''
        ]

        if not legal_moves:
            return None

        move = random.choice(legal_moves)
        return f'{move[0] + 1} {move[1] + 1}'

def save_q_table(q_table):
    # Save Q-table
    with open('q_table.pkl', 'wb') as f:
        pickle.dump(q_table, f)

def train_q_learning_algorithm(episodes, ai_1, ai_2=None):
    ai_1_symbol =  ai_1.get_ai_symbol()
    ai_2_symbol =  'X' if ai_1_symbol == 'O' else 'O'

    if ai_2 is None:
        ai_2 = RandomAI(symbol=ai_2_symbol)

    ai_1_win_count = 0
    ai_2_win_count = 0
    draw_count = 0

    for i in range(episodes):
        game = TicTacToe()
        winner = game.play_game(ai_1, ai_2, training_flag=True)

        if winner == ai_1_symbol:
            ai_1_win_count += 1
        elif winner == ai_2_symbol:
            ai_2_win_count += 1
        else:
            draw_count += 1

    print('Games played: ', episodes)
    print('QLearning: ', ai_1_win_count, ' wins')
    print('Opponent: ', ai_2_win_count, ' wins')
    print('Draws: ', draw_count)

    print('Would you like to save the q_table?')
    select = input('>> ').strip()

    if select == 'y':
        save_q_table(ai_1.get_q_table())
        print('q table saved.')
    elif select == 'n':
        print('q table not saved.')
    else:
        print('q table not saved.')
    return
