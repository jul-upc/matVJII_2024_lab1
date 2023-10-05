import numpy as np
from typing import Tuple

def naive_forward_elimination(A: np.ndarray, b: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Forward elimination function wich does NOT uses partial pivoting
     """


    # TODO: your code here!
    return (np.zeros((1,1)), np.zeros((1,1)))

def forward_elimination(A: np.ndarray, b: np.ndarray) -> Tuple[np.ndarray, np.ndarray, bool]:
    """
    Optimized forward elimination function wich uses partial pivoting
    """


    # TODO: your code here!
    return (np.zeros((1,1)), np.zeros((1,1)), False)


def backtracking(At: np.ndarray, bt: np.ndarray) -> np.ndarray:
    """
    Backtracking(At, bt) takes a triangular and regular matrix At, and an 
    independent term bt as input and produces a vector with the solution of such 
    system.
    """


    # TODO: your code here!
    return np.zeros((1,1))

