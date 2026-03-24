import numpy as np
def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.asarray([x], dtype=float)
    sig=np.zeros(len(x))
    sig = 1/(1+np.exp(-x))
    return sig