from tic_tac_toe import TicTacToe
from rule_based.rule_based_model import RuleBasedModel
from minimax.minimax_model import MinimaxModel
from q_learning.q_learning import QLearningAlgorithm
import random

SYMBOL_MAP = {
    '1' : 'O',
    '2' : 'X'
}


def main():
    game = TicTacToe()

    print('Welcome to Tic-Tac-Toe!')
    print('Please select your opponent:')
    print('1. Rule Based AI')
    print('2. Minimax AI')

    number = random.choice(['1', '2'])
    ai_symbol = SYMBOL_MAP[number]
    human_symbol = 'O' if ai_symbol == 'X' else 'X'

    choice = input('>> ').strip()

    ai = None
    if choice == '1':
        ai = RuleBasedModel(
            ai_symbol=ai_symbol,
            opponent_symbol=human_symbol
        )

    if choice == '2':
        ai = MinimaxModel(ai_symbol=ai_symbol)

    game.play_game(ai)


if __name__ == "__main__":
    main()
