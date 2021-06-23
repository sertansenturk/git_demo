import numpy as np
import pandas as pd


ARR_COLUMNS = ["A", "B", "C"]


def read_array(arr: np.array) -> pd.DataFrame:
    """[summary]

    Args:
        arr (np.array): [description]

    Returns:
        pd.DataFrame: [description]
    """
    if not isinstance(arr, np.ndarray):
        raise ValueError("arr should be an array")

    size = arr.shape
    indices = np.arange(0, size[0]) * 10
    return pd.DataFrame(arr, index=indices, columns=ARR_COLUMNS)
