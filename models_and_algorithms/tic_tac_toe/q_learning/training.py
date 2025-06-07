import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(BASE_DIR)
from tic_tac_toe import TicTacToe


def train_q_learning_algorithm(ai_1, ai_2, episodes):
    ai_1_symbol =  ai_1.get_ai_symbol()
    ai_2_symbol = ai_2.get_ai_symbol()

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
    print('RuleBased: ', ai_2_win_count, ' wins')
    print('Draws: ', draw_count)

    return
