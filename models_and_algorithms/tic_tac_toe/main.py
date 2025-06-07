from tic_tac_toe import TicTacToe
from rule_based.rule_based_model import RuleBasedModel
from minimax.minimax_model import MinimaxModel
from q_learning.q_learning import QLearningAlgorithm
import q_learning.training as training
import random
import argparse

SYMBOL_MAP = {
    '1' : 'O',
    '2' : 'X'
}


def main():
    game = TicTacToe()
    parser = \
        argparse.ArgumentParser(description="Play tic_tac_toe")
    parser.add_argument('--episodes', type=int, default=100,
            help='Number of episodes (games to simulate) for training')
    args = parser.parse_args()

    print('Welcome to Tic-Tac-Toe!')
    print('Please select your opponent:')
    print('1. Rule Based AI')
    print('2. Minimax AI')
    print('3. QLearning')
    print('4. Train QLearning Algorithm')

    number = random.choice(['1', '2'])
    ai_symbol = SYMBOL_MAP[number]
    opponent_symbol = 'O' if ai_symbol == 'X' else 'X'

    choice = input('>> ').strip()

    ai_1 = None
    if choice == '1':
        ai_1 = RuleBasedModel(
            ai_symbol=ai_symbol,
            opponent_symbol=opponent_symbol
        )
    elif choice == '2':
        ai_1 = MinimaxModel(ai_symbol=ai_symbol)

    elif choice == '3':
        ai_1 = QLearningAlgorithm(ai_symbol=ai_symbol)
    elif choice == '4':
        print('Training QAlgorithm against RuleBasedModel')
        training.train_q_learning_algorithm(
            ai_1=QLearningAlgorithm(ai_symbol=ai_symbol),
            ai_2=RuleBasedModel(ai_symbol=opponent_symbol, opponent_symbol=ai_symbol),
            episodes=args.episodes
        )

    else:
        print('Invalid input, exiting program.')
        return

    if choice != '4':
        game.play_game(ai_1, ai_2=None)


if __name__ == "__main__":
    main()
