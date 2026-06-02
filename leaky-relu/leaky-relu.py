import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    x = np.asarray(x)
    relu_val = np.where(x >= 0, x, alpha*x) #element-wise conditional operations.

    return relu_val