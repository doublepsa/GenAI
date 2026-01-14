
# Lecture 5: GPT

## Generative Pretrained Transformer

As an example, this is the training regime of InstructGPT (precursor to chatGPT):

### 1. Train initial model with supervised learning with demonstration data

given input, shown desired output

### 2. Train seperate reward model using labelers

output is ranked by labeler to determine reward
Labelers had a set of criteria to judge the output

-   overall quality (1-7)
-   follows instructions
-   hallucination
-   contains inadmissable content
-   etc.

### 3. Improve initial model with reinforcement learning using reward model

Used proximal policy optimization (PPO)
stochastic optimal control
an action changes the state of the system. Each state has a reward itself, and can (potentially) lead to futher rewards by giving access to other states
Reinforcement learning finds the optimal set of actions to maximize reward
In more detail - agent must choose action that has greatest return, given by the expected value of the sum of all (discounted) future rewards, if that action is taken at this time

1.  Markov decision process

    Reinforcement learning is equivalent to finding an optimal graph traversal where nodes are states, edges are actions, and weights are rewards
    Note: reinforcement learning uses discounted return, the return function is the current reward plus a percent of the return from the resultant state.
    Ensuring the percent is never 1 ensures reward is always finite
    Alternatively, only look ahead a finite number of actions

2.  q-learning

    q<sub>&pi;</sub>(s,a): action-value function, expected discounted return when starting at state s, taking action a and then following policy &pi;.
    optimizing q is one way to do reinforcement learning

3.  policy-gradient methods

    policy is parameterized A x S x &Theta; -> [0,1]
    where &pi;<sub>&Theta;</sub>(a|s) = &pi;(a|s,&theta;), where &theta; is a vector. we seek a parameter that corresponds to the optimal policy
    Optimize a performance measure such as expected return when following policy given starting state determined by a random distribution
    This can be maximized with, for example, stochastic gradient ascent
