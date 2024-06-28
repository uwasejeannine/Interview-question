# Given a dictionary with weights, write a function random_key that returns a key at random with a probability proportional to the weights.

# Input:
# weights = {'A': 1, 'B': 2}
# Output:
# random_key(weights) -> return A 1/3 of the time, B 2/3 of the time

import random

def random_key(weights):
    """
    Returns a key at random with a probability proportional to the weights.
    """
    keys = list(weights.keys())
    weights_list = list(weights.values())
    return random.choices(keys, weights=weights_list)[0]

weights = {'A': 1, 'B': 2}

# Test the function
for _ in range(10):
    print(random_key(weights))
