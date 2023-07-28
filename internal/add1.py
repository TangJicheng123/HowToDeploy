import numpy as np


def my_add_func(x: str) -> str:
    x_int = int(x)
    x_int += 1
    y = str(x)
    print(np.__version__)
    return y