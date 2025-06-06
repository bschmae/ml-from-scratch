# Minimax Algorithm for Tic-Tac-Toe

The **Minimax algorithm** is a recursive decision-making strategy used to choose the optimal move in two-player games like Tic-Tac-Toe. It assumes both players play optimally.


**Minimax** is used in zero-sum games to denote minimizing the opponent's maximum payoff. In a zero-sum game, this is identical to minimizing one's own maximum loss, and to maximizing one's own minimum gain.

For every two-person zero-sum game with finitely many strategies, there exists a value V and a mixed strategy for each player, such that

(a) Given Player 2's strategy, the best payoff possible for Player 1 is V, and
(b) Given Player 1's strategy, the best payoff possible for Player 2 is −V.
Equivalently, Player 1's strategy guarantees them a payoff of V regardless of Player 2's strategy, and similarly Player 2 can guarantee themselves a payoff of −V. The name minimax arises because each player minimizes the maximum payoff possible for the other – since the game is zero-sum, they also minimize their own maximum loss

## Goal

Enable the AI player to choose the move that maximizes its chance of winning or, at worst, forces a tie—assuming the opponent also plays optimally.

## Core Idea

- The AI (e.g. `O`) tries to **maximize** the score.
- The opponent (e.g. `X`) tries to **minimize** the score.

Minimax explores all possible future game states to evaluate the best move based on the outcome of each.

## Scoring Terminal States

- AI wins → `+1`
- Opponent wins → `-1`
- Tie → `0`

These scores are used as the **base case** for recursion.

## Recursive Strategy

1. **Check for terminal state** (win, lose, or tie):
   - Return the corresponding score.

2. **Simulate all possible moves**:
   - For each empty cell:
     - Make the move.
     - Recursively call `minimax` for the next player.
     - Undo the move.

3. **Choose the best move**:
   - If it's AI's turn → return the move with the **maximum score**.
   - If it's opponent's turn → return the move with the **minimum score**.

## Example Flow

```text
AI's Turn (Maximizing)
 ├─ Move 1 → Min Turn
 │    ├─ Move A → Max Turn
 │    │    └─ Terminal → Score
 │    └─ Move B → Max Turn
 │         └─ Terminal → Score
 └─ Move 2 → Min Turn
      └─ ...
