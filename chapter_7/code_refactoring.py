import numpy as np
import pandas as pd
from pandas.testing import assert_series_equal
import pytest
import math

# def calculate_ratio(
#     df: pd.DataFrame, col1: str, col2: str
# ) -> pd.Series:
#     # You want to change from this:
#     return df[col1] / df[col2]
#     # To this:
#     # return np.divide(df[col1], df[col2])

def calculate_ratio(
    df: pd.DataFrame, col1: str, col2: str
) -> pd.Series:
    return np.divide(df[col1], df[col2])


def test_calculate_ratio():
    data = pd.DataFrame({"sales": [100, 200], "cost": [50, 100]})
    expected = pd.Series([2.0, 2.0])
    output = calculate_ratio(data, "sales", "cost")
    assert_series_equal(output, expected)
    

def calculate_distance(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
    """Calculate 3D distance between two points."""
    return math.sqrt(
        (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
    )

def test_calculate_distance_positive_coordinates():
    assert calculate_distance(1, 2, 3, 4, 5, 6) == pytest.approx(
        5.19, abs=1e-2
        )

def test_calculate_distance_negative_coordinates():
    assert calculate_distance(
        -1, -2, -3, -4, -5, -6
    ) == pytest.approx(5.19, abs=1e-2)

def test_calculate_distance_zero_coordinates():
    assert calculate_distance(0, 0, 0, 0, 0, 0) == 0.0


def test_calculate_distance_invalid_inputs():
    with pytest.raises(TypeError):
        calculate_distance("1", 2, 3, 4, 5, 6)

!pytest code_refactoring.py