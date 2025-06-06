import random
class QLearningAlgorithm():
    def __init__(self, ai_symbol):
        self.q_table = {}
        self.gamma =  0.9 # discount factor
        self.alpha = 0.1  # learning rate
        self.epsilon = 1.0 # exploration rate
        self.min_epsilon = 0.1
        self.epsilon_decay_rate = 0.1
        self.ai_symbol = ai_symbol
        self.human_symbol = 'O' if ai_symbol == 'X' else 'X'

    def get_ai_symbol(self):
        return self.ai_symbol

    def get(self, state, action):
        return self.q_table.get(state, {}).get(action, 0.0)

    def set(self, state, action, value):
        if state not in self.q_table:
            self.q_table[state] = {}
        self.q_table[state][action] = value

    def make_move(self, board):
        state = tuple(cell for row in board for cell in row)
        legal_moves = []
        action = None

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == '':
                    legal_moves.append([i, j])

        # exploration - greedy policy
        if random.random() < self.epsilon:
            if self.epsilon > self.min_epsilon :
                self.epsilon = self.epsilon * self.epsilon_decay_rate
                action = random.choice(legal_moves)

                self.set(state, action, 0.0)
            return action

        # exploitation
        q_values = {}
        for move in legal_moves:
            q_values[tuple(move)] = self.get(state, tuple(move))

        # Choose the move with the highest Q-value
        return max(q_values, key=q_values.get)
