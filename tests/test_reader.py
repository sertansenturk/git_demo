import numpy as np
import pandas as pd
import pytest
from tutorial import reader


class TestReader:
    def test_read_array(self):
        # GIVEN
        arr = np.array([[1, 2, 3], [2, 3, 4]])

        # WHEN
        result = reader.read_array(arr)

        # THEN
        expected = pd.DataFrame(
            data=arr, index=[0, 10], columns=["A", "B", "C"]
        )  # 2x3 table
        pd.testing.assert_frame_equal(result, expected)

    def test_read_array_not_array(self):
        # GIVEN
        arr = "sertan"

        # WHEN
        with pytest.raises(ValueError):
            reader.read_array(arr)
