# Model-Free Reinforcement Learning alrgorithm for Tic-Tac-Toe

## Overview: Model-Free Reinforcement Learning

Model-free reinforcement learning (RL) focuses on learning directly from interaction with the environment **without explicitly building an internal model** of it.

- This approach is simpler in environments where building an accurate model is challenging.
- The agent learns through **trial and error**, discovering which actions lead to better outcomes by experiencing the consequences of its actions.
- Model-free RL is well-suited for **dynamic environments** where rules might change.
- However, learning solely through trial and error can be **less sample-efficient** compared to model-based approaches.

In this context, we focus on one popular model-free RL method: **Q-Learning**.

---

## Q-Learning

Q-Learning learns a **Q-value** for each state-action pair. The Q-value represents the **expected future reward** of taking a specific action in a particular state.

- The agent chooses actions with the **highest Q-values** to maximize long-term rewards.
- Over time, it improves decision-making by updating a **Q-table**, which stores Q-values for state-action pairs. The Q-table is essentially a memory structure where the agent stores information about which actions yield the best rewards in each state and updates it as it continues to learn. The Q-table helps the agent make informed decisions by showing which actions are likely to lead to better rewards.

---

## Key Components of Q-Learning

### I. Q-Values (Action-Values)

- Q-values estimate the expected rewards for taking an action in a given state.
- These values are updated using the **Tempo ral Difference (TD) update rule**.

### II. Rewards and Episodes

- The agent moves through states by taking actions and receiving rewards.
- Each sequence continues until reaching a **terminal state**, which ends the episode.

### III. Temporal Difference (TD) Update Rule

The core Q-value update (Temporal Difference) formula is:

Q(S, A) ← Q(S, A) + α ( R + γ * max_a′ Q(S′, a′) − Q(S, A) )

Where:

| Symbol | Meaning                                                                                      |
|--------|----------------------------------------------------------------------------------------------|
| \( S \)  | Current state                                                                               |
| \( A \)  | Action taken by the agent                                                                   |
| \( S' \) | Next state after taking action \( A \)                                                     |
| \( a' \) | Possible next actions in state \( S' \) (used to select the best next action)               |
| \( R \)  | Reward received for taking action \( A \) in state \( S \)                                 |
| (γ) (Gamma) | **Discount factor** balancing immediate and future rewards. A higher value makes the agent consider future rewards more strongly. Between 0 and 1                     |
| (α) (Alpha) | **Learning rate** determining the influence of new information on old Q-values. A lower value makes learning more stable but slower. Between 0 and 1      |


### 4. ϵ-greedy Policy (Exploration vs. Exploitation)

The agent decides which action to take based on the **ϵ-greedy policy**:

- **Exploitation:** With probability (1 - ϵ), the agent selects the action with the highest Q-value, leveraging its current knowledge to maximize rewards.
- **Exploration:** With probability (ϵ), the agent chooses a random action, allowing it to explore new strategies and improve its policy over time.

Controls randomness: higher at first to explore, lower later to exploit learned Q-values.

---

This balance between exploration and exploitation helps the agent efficiently learn optimal strategies, especially in complex games like Tic-Tac-Toe.

Q-Learning models follow an iterative process where various components interact to train the agent effectively.

- **Agent:**  
  The decision-maker that takes actions within the environment.

- **States:**  
  Variables defining the agent’s current position or situation in the environment.

- **Actions:**  
  Operations the agent can perform when in a specific state.

- **Rewards:**  
  Feedback received after taking an action, guiding the agent toward desirable outcomes.

- **Episodes:**  
  A sequence of actions starting from an initial state and ending when a terminal state is reached.

- **Q-values:**  
  Estimates of the expected reward for each state-action pair.

---

### Steps of Q-Learning

**I. Initialization:**
   The agent begins with an initial Q-table, where all Q-values are typically set

**II. Exploration:**
   The agent selects an action based on the ϵ-greedy policy, balancing between:
   - **Exploration:** Choosing a random action with probability ( epsilon ).
   - **Exploitation:** Choosing the action with the highest Q-value with probability \( 1 - epsilon \).

**III. Action and Update:**
   - The agent performs the selected action.
   - Observes the next state and receives a reward.
   - Updates the Q-value for the state-action pair using the Temporal Difference (TD) update rule

**IV. Iteration:**
   The process repeats for many episodes until the agent converges on an optimal policy.

---

This iterative loop allows the agent to improve its strategy over time by continuously updating its Q-values based on new experiences.

**Temporal Difference** is calculated by comparing the current state and action values with the previous ones. It provides a way to learn directly from experience, without needing a model of the environment.

## Bellman’s Equation: Foundation of Q-Learning

Although Q-learning is a **model-free** reinforcement learning method, it is still grounded in the **Bellman Optimality Equation**.

Bellman’s equation is a fundamental concept in reinforcement learning and dynamic programming. It provides a recursive decomposition for the **value function**, expressing the value of a state in terms of the rewards and values of successor states.

### What is Bellman’s Equation?

In the context of reinforcement learning, the value function \( V(s) \) represents the expected cumulative reward an agent can achieve starting from state \( s \) and following a certain policy thereafter.

Bellman’s equation expresses \( V(s) \) as:

V(s) = max_a [ R(s, a) + γ × Σ_s' P(s' | s, a) × V(s') ]

Where:

| Symbol       | Meaning                                                                                 |
|--------------|-----------------------------------------------------------------------------------------|
| \( V(s) \)   | Value of state \( s \) — expected future reward starting from \( s \)                   |
| \( a \)      | Action chosen in state \( s \)                                                         |
| \( R(s, a) \) | Immediate reward received after taking action \( a \) in state \( s \)                 |
| \( \gamma \) | Discount factor (between 0 and 1) balancing immediate and future rewards                |
| \( P(s' | s, a) \) | Probability of transitioning to state \( s' \) after taking action \( a \) in state \( s \) |
| \( s' \)     | Possible next state after the transition                                               |

### Intuition Behind Bellman’s Equation

- The value of the current state \( s \) is the **maximum expected reward** achievable by taking the best action \( a \).
- This reward consists of two parts:
  1. The **immediate reward** \( R(s, a) \) from taking action \( a \) in state \( s \).
  2. The **discounted value** of the next state \( s' \), weighted by the transition probability \( P(s'|s, a) \).

### Role in Reinforcement Learning

- Bellman’s equation provides a way to break down complex decision problems into simpler subproblems.
- Many RL algorithms, including Q-learning** and **value iteration**, use Bellman’s equation (or its variants) to iteratively estimate value functions or Q-values.
- Solving Bellman’s equation helps find an **optimal policy** that maximizes expected cumulative rewards.

---

### Key Distinction

|                | Bellman Equation                | Q-Learning                              |
|----------------|----------------------------------|------------------------------------------|
| Type           | Exact, expectation-based        | Approximate, sample-based                |
| Needs model?   | ✅ Yes (transitions, rewards)     | ❌ No (model-free)                        |
| Uses learning rate? | ❌ No                         | ✅ Yes                                    |
| Used for       | Value iteration, policy evaluation | Learning optimal action-values (Q)     |

