import pandas as pd
df = pd.DataFrame(
{"num_apples": [1, 2, 3, 0], "num_oranges": [4, 5, 0, 6]}
)
print(df)



def create_booleans(feature):
    # print(feature)
    # print(feature == 0)
    return (feature == 0) * 1


df["has_apples"] = create_booleans(df["num_apples"])
df["has_oranges"] = create_booleans(df["num_oranges"])
print(df)


import pytest
import pandas as pd
from pandas.testing import assert_frame_equal

def create_booleans(feature):
    return (feature == 0) * 1


def test_create_booleans():
    df = pd.DataFrame(
        {"num_apples": [1, 2, 3, 0], "num_oranges": [4, 5, 0, 6]}
    )
    expected_df = pd.DataFrame(
        {"has_apples": [1, 1, 1, 0], "has_oranges": [1, 1, 0, 1]}
    )
    df["has_apples"] = create_booleans(df["num_apples"])
    df["has_oranges"] = create_booleans(df["num_oranges"])
    assert_frame_equal(
        df[["has_apples", "has_oranges"]], expected_df
    )

test_create_booleans()




def calculate_average(nums: list) -> float:
    """Calculate average - has edge case with empty list."""
    return sum(nums) / len(nums)


print(calculate_average([]))


import pytest

def calculate_average(nums: list) -> float:
    """Calculate average - has edge case with empty list."""
    return sum(nums) / len(nums)

def test_calculate_average_positive_numbers():
    assert calculate_average([1, 2, 3, 4, 5]) == 3

def test_calculate_average_empty_list():
    assert calculate_average([]) == 0



# import math

# def calculate_distance(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
#     """Calculate 3D distance between two points."""
#     return math.sqrt(
#         (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
#     )































