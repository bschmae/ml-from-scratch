# Intelligent Agents

### I. Agents and Environments

An **agent** is anything that can be understood as perceiving its environemnt through sensors
and acting upon its environment with actuators.

The **envionment** is the entire universe! Well, not really. The universe is obviously too big
for us to deal with in any practical way, thus, when it comes to AI, the environemnt
is the the narrow part of the universe whose state is relevant to designing the agent and
that affects what the agent perceives and interacts with.

A **percept** is used to refer to the subject content an agent is perceiving.

The complete history of everything that an agent has ever perceived is called its **percept sequence**.

> "An agent's choice of action at any given instant can depend on its built-in-knowledge and on the entire percept
sequence observed to date, but not on anything it hasn't perceived.

The **agent function** maps any given percept sequence to an action;
it is an abstract mathematical way to describe the agent's behavior. 
Internally, the agent function is implemented by an **agent program**. That is,
the agent program is a concrete implementation, running on some physical system.

### II. Rationality

A rational agent is one that does the right thing. Simple enough, right?

That depends on what we mean by the right thing - a question of moral philosophy
that has many proposed ideas. AI, however, has generally adhered to one notion when
evaluating an agent.

**Consequentialism** is the evaluation of an agent's behavior by the outcomes it produces — that is, the consequences of its actions. The more desirable the consequences, the better.

Desirability of an outcome is captured by a **performance measure** which analyzes and 
evaluates any given sequence of environment states. Desirability is an entirely subjective notion
and can therefore be a contentious and complex matter to deal with.
- Performance measures can be **explicit**, meaning the agent has a built-in representation of them.
- Or they can be **implicit**, meaning the agent learns them through feedback, such as rewards.

The purpose we encode into a machine should match the purpose we truly want it to achieve—but formulating the **performance measure** correctly can be challenging.

As a general rule, design performance measures to capture **what you actually want accomplished in the environment**, rather than prescribing a specific set of behaviors you expect the agent to follow.

Formal definition of a **rational agent**
*For every possible percept sequence, a rational agent selects the action that maximizes its expected performance measure, given (i) the evidence contained in that percept sequence and (ii) whatever built-in knowledge the agent possesses.*

---

## III. The Nature of Environments

A **task environment** is the problem setting in which a rational agent operates.

### Key Properties of Environments

| Property | Variants | Meaning |
|----------|----------|---------|
| **Observability** | *Fully observable*  | The agent’s sensors provide complete, accurate access to the true state of the environment at each time step. |
| | *Partially observable* | Some aspects of the true state are hidden or noisy, e.g., due to limited or faulty sensors. |
| | *Unobservable* | The agent receives no percepts at all. |
| **Number of agents** | *Single-agent* | Only one agent acts in the environment. |
| | *Multi-agent* | Multiple agents act and interact.<br>• **Competitive**: agents pursue conflicting goals (e.g., chess).<br>• **Co-operative**: agents share a common goal (e.g., robotic swarm).<br>• **Mixed**: partly aligned, partly conflicting interests (e.g., autonomous traffic). |
| **State evolution** | *Deterministic* | The next state is fully determined by the current state and the chosen action(s). |
| | *Nondeterministic* | Multiple successor states are possible, but without quantified probabilities. |
| | *Stochastic* | Successor states are governed by known probability distributions. |
| **Temporal structure** | *Episodic* | Experience is a sequence of independent episodes: percept → single action → reward. Earlier episodes do not affect later ones. |
| | *Sequential* | Current decisions influence future states and rewards; the agent must plan ahead. |
| **Dynamics during deliberation** | *Static* | The environment does not change while the agent is deliberating. |
| | *Dynamic* | The environment may evolve while the agent is choosing its action (real-time settings). |
| **State & action granularity** | *Discrete* | States, time steps, and actions are countable (e.g., grid world, turn-based games). |
| | *Continuous* | States or actions vary along real-valued dimensions (e.g., robot joint angles, continuous time). |
| **Knowledge of models** | *Known* | The agent has an accurate model of state transitions and outcome probabilities. |
| | *Unknown* | The agent must learn or infer the environment’s dynamics from experience. |

An accurate characterization of the task environment guides the choice of algorithms and representations, helping to ensure that the agent’s design is both efficient and effective.
