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

### III. The Nature of Environments

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

### IV. The Structure of Agents

**Agent architecture** is the physical computing system with sensors and actuators.  
**Agent program** is the software that implements the agent function.

> `agent = architecture + program`

---

### Table-Driven Agents

The **table-driven approach** to agent construction involves creating a lookup table that maps every possible percept sequence to an action. While this can theoretically produce a functional agent, it is ultimately **impractical**.

Let `P` be the set of possible percepts and `T` be the agent's lifetime (i.e. the total number of percepts it will receive). The lookup table would need to contain:

> ∑ (from t = 1 to T) |P|^t entries

Even in relatively simple environments, this results in a table of **astronomical size**, making storage and computation infeasible.

Despite its impracticality, the table-driven model is instructional. It highlights a central challenge in AI:

> *How can we design a compact program that generates rational behavior, without relying on an unmanageably large lookup table?*

**Pseudocode**

**function** TABLE-DRIVEN-AGENT(*percept*) **returns** an action
  **persistent**: *percepts*, a sequence, intitially empty *table*,
              a table of actions, indexed by percept sequences, initially
              fully specified

  append *percept* to the end of *percepts*
  *action* <-- LOOKUP(*percepts*, *table*)
  **return** *action*

---

### Simple Reflex Agents

These agents ignore percept history and base their decisions solely on the current percept. The mapping from percepts to actions is based on **condition-action rules**, typically written as:

> `if some condition x then do action y`

These rules can apply beyond simple reflex agents and may also be **learned or hard-coded** in more complex models.

**Pseudocode**

**function** SIMPLE-REFLEX-AGENT(*percept*) **returns** an action
  **persistent**: *rules*, a set of condition-action rules

  *state* <-- INTERPRET-INPUT(*percept*)
  *rule* <-- RULE-MATCHING(*state*, *rules*)
  *action* <-- *rule*.ACTION
  **return** *action*

---

### Model-Based Reflex Agents

Model-based reflex agents maintain an **internal state** that depends on the history of percepts. This helps handle **partial observability** by keeping track of parts of the world the agent cannot currently perceive.

To do this effectively, these agents rely on:

- A **transition model**: Knowledge of how the world changes over time.
  - How the world changes independently of the agent.
  - How the agent’s actions affect the environment.

- A **sensor model**: Knowledge of how the agent’s percepts relate to the actual world state.

These models together help the agent update its internal state and act more intelligently.

**Pseudocode**

**function** MODEL-BASED-REFLEX-AGENT(percept) **returns** an action
  **persistent**: *state*, the agent's current conception of the world state, *transition_model*, a description of how the next state depends on the current state and action, *sensor_model*, a description of how the current world state is reflected in the agent's percepts
  *rules*, a set of condition-action rules, *action*, the most recent action, intially none

  *state* <-- UPDATE-STATE(*state*, *action*, *percept*, *transition_model*, *sensor_model*)
  *rule* <-- RULE-MATCH(*state*, *rules*)
  *action* <-- *rule*.ACTION
  **return** *action*

---

### Goal-Based Agents

In addition to internal models, goal-based agents incorporate **goals**—desirable outcomes that guide decision-making.

- Sometimes goals can be achieved with a single action.
- More often, achieving a goal requires evaluating **action sequences** or considering **long-term consequences**.

This gives rise to the fields of **search** and **planning**, which focus on finding sequences of actions that achieve the agent's goals.

---

### Utility-Based Agents

Goals distinguish between “good” and “bad” states but are too crude for many complex situations. Instead, utility-based agents use a **utility function**, which internalize the performance meassure for various states or outcomes.

Utility functions enable:

- Choosing between multiple ways to achieve a goal.
- Making decisions under **uncertainty**, where multiple outcomes are possible.

A rational agent chooses the action that maximizes **expected utility**—the average utility value of all possible outcomes weighted by their probabilities.

---

### Learning Agents

Learning enables agents to improve their behavior over time, especially in unknown or changing environments.

A learning agent typically includes four key components:

1. **Learning element** – Makes improvements to the agent’s behavior.
2. **Performance element** – Chooses external actions based on current knowledge.
3. **Critic** – Evaluates the agent's performance and provides feedback.
4. **Problem generator** – Suggests exploratory actions to gather new, informative experiences. The problem generator is important because it allows the agent to explore and perhaps do some suboptimal actions in the short term, which could lead to discoveries that lead to much better actions in the long term.

> Learning involves adjusting these components to better align with the feedback received from the environment, ultimately improving the agent’s overall performance.

---
