import numpy as np

# game rules
probs = [
    [0.99, 0],
    [0.9, 0],
    [0.8, 0],
    [0.7, 0],
    [0.6, 0],
    [0.5, 0],
    [0.4, 1],  # quit with 1 as the action
    [0.3, 0],
    [0.2, 0],
    [0.1, 0]
]
rewards = [
    [100, 0],
    [500, 0],
    [1000, 0],
    [5000, 0],
    [10000, 0],
    [50000, 0],
    [100000, 0],
    [500000, 0],
    [1000000, 0],
    [5000000, 0]
]

# MDP parameters
gamma = 0.9  # discount factor
theta = 1e-6  # convergence threshold
num_states = len(probs) + 1  # include terminal state
num_actions = 2  # play or quit
transitions = [[i+1, num_states-1] for i in range(num_states-1)]  # deterministic transitions to next state

# value iteration
V = np.zeros(num_states)
max_iterations = 100
for i in range(max_iterations):
    delta = 0
    for s in range(1, num_states):  # exclude terminal state 10
        v = V[s]
        max_value = -float("inf")
        for a in range(num_actions):
            value = probs[s-1][a] * (rewards[s-1][a] + gamma * V[transitions[s-1][a]])
            if value > max_value:
                max_value = value
        V[s] = max_value
        delta = max(delta, abs(v - V[s]))
    if delta < theta:
        break

# extract optimal policy
policy = np.zeros(num_states, dtype=int)
for s in range(1, num_states-1):  # exclude terminal states
    max_value = -float("inf")
    for a in range(num_actions):
        value = probs[s-1][a] * (rewards[s-1][a] + gamma * V[transitions[s-1][a]])
        if value > max_value:
            max_value = value
            policy[s] = a

# print optimal policy
for s in range(1, num_states):
    print("Stage {}: {}".format(s, "Quit" if policy[s] else "Play"))