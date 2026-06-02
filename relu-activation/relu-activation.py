import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    x = np.asarray(x)
    relu_val = np.maximum(0,x) #element-wise maximum between 0 and input values.
    return relu_val