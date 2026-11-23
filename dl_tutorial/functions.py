# step function
def step_function(x):
    return 1 if x > 0 else 0

import numpy as np
def step_function(x):
    return np.array(x > 0, dtype=int)

if __name__ == "__main__":
    x = np.array([-1, 1, 2])
    print(step_function(x))