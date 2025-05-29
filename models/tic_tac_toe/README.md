Tic-Tac-Toe AI

1. The Problem Space
    Tic-Tac-Toe is a finite, fully obseravable, zero-sum, turn based game.

    • Finite: the game as a limited number of possible states and moves and 
    it always ends. 

    • Fully observable: if an agent has access to the complete state 
    of the environment at each point in time, then we say the task environment
    is fully observable.

    • Zero-sum: one player's gain is another player's loss. Total utility is
    always zero.

    It is a 3x3 turn based game between two players. The game ends when:
    - One player aligns three symbols horizaontally, vertically, or diagonally.
    - All cells are filled (draw).

2. State Representation
    A state in this context is the entire condition of the game at a moment in time

    The board is represented as a 3x3 grid or a 9-element array:
    - 'O' for player O
    - 'X' for player X
    - '' for an empty cell
    
    Whose turn it is: 'O' or 'X'

    Each move leads to a new state. The full set of these states and
    transitions forms what’s called the state space.

3. Action Space
    What move should I make?

    This should be a list of all possible moves it can make.
    In this context these are simply the empty squares on the board. The 
    key part is that the model has to evaluate each possible move and decide
    which is best.

4. Decision Making
    Various approaches to building an intelligent player.

    (a) Rule-Based Strategy
        - actions and decisions are guided by a set of predefined rules in
        lieu of subjective judgements.

        Simple human like rules:
            • Win in you can.
            • Block your opponent if they can win.
            • Take the center if it's open.
            • Then corners.
            • Then edghes.
        
        fast and simple, but not flexible or adaptive.
    
    (b) Search-Based Strategy (MiniMax)
        This approach simulates the rest of the game from the current state.

        • The AI plays out all possible moves both it and the opponent could
        play.
        • Assumes the opponent is playing perfectly.
        • Scores each outcome: win, draw, loss.
        • Then it chooes the move that leads to the best, worst-case outcome.

        This is a brute-force logical strategy that guarantees optimal play.
        If both players use MiniMax, the game will always end in a draw.

    (c) Learning-Based Strategy (Reinforcement Learning)
        This is where the AI learns from experience.

        • It plays games repeatedly - agaisnt itself or others.
        • Starts out making random moves.
        • Over time, it learns which moves lead to better outcomes.
        • It builds a policy (mental model) for how to act in different
        situations.

        This method is more advanced and generalizable.
        It doesn't start out smart, but it gets smarter over time.

5. Optimizing and Reducing Complexity
    Many states in Tic-Tac-Toe are duplicates due to symmetry (rotated or 
    mirrored versions of the same board). By recognizing these duplicates you 
    can simplify your AI's job.

    This is important for:
    • Saving memory in learning models.
    • Reducing the number of decisions to evaluate in search strategies.