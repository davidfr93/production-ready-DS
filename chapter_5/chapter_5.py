import pandas as pd
import numpy as np

def standardize_features(X):
    """Standardize the features in the input data."""
    X_standardized = (X - X.mean()) / X.std()
    return X_standardized


import numpy as np
X_train = np.array([5, 10, 15, 20, 25])
X_test = np.array([8, 12, 18, 22, 28])

print(X_train)
print(X_test)

def standardize_features(X):
    return (X - X.mean()) / X.std()

X_train = np.array([5, 10, 15, 20, 25])
X_test = np.array([8, 12, 18, 22, 28])
X_train_standardized = standardize_features(X_train)
X_test_standardized = standardize_features(X_test)

def calculate_average_rating(ratings, product_id):
    product_ratings = [
    r for r in ratings if r["product_id"] == product_id
    ]
    if not product_ratings:
        return None
    total_score = sum(r["score"] for r in product_ratings)
    return total_score / len(product_ratings)



def calculate_average_rating(
    ratings: list[dict[str, int]], product_id: int
    ) -> float | None:
    product_ratings = [
        r for r in ratings if r["product_id"] == product_id
        ]
    if not product_ratings:
        return None
    total_score = sum(r["score"] for r in product_ratings)
    return total_score / len(product_ratings)




def calculate_average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)

# Type error: passing string instead of integer
result = calculate_average([1, 2, "3", 4])



def parse_pipe_delimited_text(text: str) -> dict:
    parts = text.split("|")
    if len(parts) % 2 != 0:
        raise ValueError(
            "Input string must have an even number of parts"
        )
    return {parts[i]: parts[i + 1] for i in range(0, len(parts), 2)}

def parse_pipe_delimited_text(text: str) -> dict:
    """
    Parse a pipe-delimited string into a dictionary.

    Parameters
    ----------
    text: str
        A pipe-delimited string to parse

    Returns
    -------
    dict
        Dictionary with even indices as keys, odd indices as values

    Raises
    ------
    ValueError: If the input string has an odd number of parts

    Examples
    --------
    >>> parse_pipe_delimited_text("name|John|age|30")
    {'name': 'John', 'age': '30'}
    """
    parts = text.split("|")
    if len(parts) % 2 != 0:
        raise ValueError(
            "Input string must have an even number of parts"
        )
    return {parts[i]: parts[i + 1] for i in range(0, len(parts), 2)}






from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score
import numpy as np

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
train_labels = np.array([2, 4, 5, 4, 5])

kf = KFold(n_splits=5, random_state=42, shuffle=True)

model = LinearRegression()

def cv_rmse(model, X):
    return np.sqrt(
        -cross_val_score(
            model, X, train_labels,
            scoring="neg_mean_squared_error", cv=kf
        )
    )

# Calculate RMSE scores
scores = cv_rmse(model=model, X=X)
print(f"Mean RMSE: {scores.mean():.3f}")

def cv_rmse(model, X, train_labels, kf):
    rmse = np.sqrt(
        -cross_val_score(
            model, X, train_labels,
            scoring="neg_mean_squared_error", cv=kf
        )
    )
    return rmse



# Improve Code Readability
def normalize_data(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    df[columns] = (
        df[columns] - df[columns].mean()
    ) / df[columns].std()
    return df

data = pd.DataFrame(
    {
        "temperature": [25.5, 27.8, 23.2],
        "humidity": [60.0, 55.5, 62.3],
        "pressure": [1013.2, 1015.7, 1012.8],
    }
)
data

normalized_data = normalize_data(data, columns=["humidity"])
print(f"Original data:\n{data.head()}")


def normalize_data(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    df = df.copy()
    df[columns] = (df[columns] - df[columns].mean()) / df[columns].std()
    return df

# def normalize_data(df: pd.DataFrame, columns: list) -> pd.DataFrame:
#     df = df.copy()
#     df[columns] = (
#         df[columns] - df[columns].mean()
#     ) / df[columns].std()
#     return df


data = pd.DataFrame(
    {
        "temperature": [25.5, 27.8, 23.2],
        "humidity": [60.0, 55.5, 62.3],
        "pressure": [1013.2, 1015.7, 1012.8],
    }
)
data

normalized_data = normalize_data(data, columns=["humidity"])
print(f"Original data:\n{data}")
print(f"Normalized data:\n{normalized_data}")



# Avoid Using Flags As Parameters
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({"A": [1, 2, np.nan], "B": [10, 20, 30], "C": [100, 200, 300]})
df

df.to_csv("data/sample.csv", index=False)

def preprocess_data(
    df: pd.DataFrame,
    fill_missing: bool = False,
    normalize: bool = False,
    ) -> pd.DataFrame:

    if fill_missing:
        df = df.fillna(df.mean())

    if normalize:
        df = (df - df.mean()) / df.std()

    return df

df = pd.read_csv("data/sample.csv")
df

cleaned_df = preprocess_data(df, fill_missing=True, normalize=False)
cleaned_df




import pandas as pd
import numpy as np

def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    return df.fillna(df.mean())


def normalize_data(df: pd.DataFrame) -> pd.DataFrame:
    return (df - df.mean()) / df.std()

def preprocess_data(df: pd.DataFrame, steps: list) -> pd.DataFrame:
    for step in steps:
        df = step(df)
    return df



df = pd.read_csv("data/sample.csv")
df
cleaning_steps = [normalize_data, fill_missing_values]
cleaned_df = preprocess_data(df, cleaning_steps)

cleaned_df

# Extract Common Logic Into Utilities
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame(
    {
        "text": [
            "Hello, World! 123",
            "This is a TEST comment.",
            "Special @#$% characters here!",
        ],
        "user": ["user1", "user2", "user3"],
        "date": ["2023-05-01", "2023-05-02", "2023-05-03"],
    }
)
df

# Save the DataFrame to a CSV file
df.to_csv("data/comments.csv", index=False)


def clean_text_data(df: pd.DataFrame) -> pd.DataFrame:
    df["text"] = df["text"].str.lower()
    df["text"] = df["text"].str.replace(
        "[^a-zA-Z\s]", "", regex=True
    )
    df["text"] = df["text"].str.strip()
    return df

def preprocess_user_input(text: str) -> str:
    text = text.lower()
    text = "".join(
        char for char in text if char.isalnum() or char.isspace()
    )
    text = text.strip()
    return text


df = pd.read_csv("data/comments.csv")
df

cleaned_df = clean_text_data(df)
cleaned_df


user_input = "Hello, World! 123"
user_input

cleaned_input = preprocess_user_input(user_input)
cleaned_input


def clean_text(text: str) -> str:
    text = text.lower()
    text = "".join(
        char for char in text if char.isalnum() or char.isspace()
    )
    return text.strip()

def clean_text_data(df: pd.DataFrame) -> pd.DataFrame:
    df["text"] = df["text"].apply(clean_text)
    return df

def preprocess_user_input(text: str) -> str:
    return clean_text(text)


# Advanced Function Toolkit
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

data = [('Alice', 25), ('Bob', 30), ('Charlie', 22)]
print(data)
# sorted_data = sorted(data, key=lambda x: x[1])
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)

# Partial Functions
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import KFold, cross_val_score
import numpy as np


def cv_rmse(model, X, train_labels, kf):
    return np.sqrt(
        -cross_val_score(
            model, X, train_labels,
            scoring="neg_mean_squared_error", cv=kf
        )
    )


from functools import partial

# Create sample data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
print(X)
train_labels = np.array([2, 4, 5, 4, 5])
print(train_labels)

kf = KFold(n_splits=5, random_state=42, shuffle=True)

# Create a partial function with fixed X, train_labels, and kf
cv_rmse_with_data = partial(
    cv_rmse, X=X, train_labels=train_labels, kf=kf
)

# Call the partial function with Linear Regression
linear_scores = cv_rmse_with_data(model=LinearRegression())

# Call the partial function with Ridge Regression
ridge_scores = cv_rmse_with_data(model=Ridge(alpha=0.5))


# *args and **kwargs
import numpy as np
from typing import Callable


def transform_pipeline(
    data: np.ndarray, *transformers: Callable
) -> np.ndarray:
    for transformer in transformers:
        data = transformer(data)
    return data

def log_transform(data: np.ndarray) -> np.ndarray:
	return np.log1p(data)


def standardize(data: np.ndarray) -> np.ndarray:
	return (data - data.mean()) / data.std()


raw_data = np.random.rand(100, 5) * 100
print(raw_data[:5,:])

transformed_data = transform_pipeline(
	raw_data, log_transform, standardize
)
print(transformed_data[:5,:])


import numpy as np
from typing import Callable


def transform_pipeline(
    data: np.ndarray, **transformers: dict[str, Callable]
) -> np.ndarray:
    for transformer_name, transformer_func in transformers.items():
        if not callable(transformer_func):
            raise ValueError(
                f"{transformer_name} is not callable"
            )

        data = transformer_func(data)
    return data

# def transform_pipeline(data: np.ndarray, **transformers: dict[str, Callable]) -> np.ndarray:
#     for transformer_name, transformer_func in transformers.items():
#         if not callable(transformer_func):
#             raise ValueError(f"{transformer_name} is not callable")
        
#         data = transformer_func(data)
        
#     return data

def log_transform(data: np.ndarray) -> np.ndarray:
    return np.log1p(data)


def standardize(data: np.ndarray) -> np.ndarray:
    return (data - data.mean()) / data.std()

raw_data = np.random.rand(100, 5) * 100
print(raw_data[:5,:])

transformed_data = transform_pipeline(
    raw_data,
    log_transform=log_transform,
    standardize=standardize,
)
print(transformed_data[:5,:])

# Python Decorators in Data Science
import time
from typing import Callable, List, Union
import numpy as np


def timer_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Function {func.__name__} took "
            f"{end_time - start_time:.2f} seconds to execute."
        )
        return result

    return wrapper

@timer_decorator
def train_model(X: np.ndarray, y: np.ndarray | list[float]) -> None:
    """Simulating a time-consuming model training process"""
    time.sleep(2)


if __name__ == "__main__":
    X = np.random.rand(1000, 10)
    y = np.random.rand(1000)
    train_model(X, y)


print(f"name: {train_model.__name__}")
print(f"doc: {train_model.__doc__}")
print(f"annotations: {train_model.__annotations__}")



from functools import wraps

def timer_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Function {func.__name__} took "
            f"{end_time - start_time:.2f} seconds to execute."
        )
        return result

    return wrapper



@timer_decorator
def train_model(X: np.ndarray, y: np.ndarray | list[float]) -> None:
    """Simulating a time-consuming model training process"""
    time.sleep(2)


if __name__ == "__main__":
    X = np.random.rand(1000, 10)
    y = np.random.rand(1000)
    train_model(X, y)

print(f"name: {train_model.__name__}")
print(f"doc: {train_model.__doc__}")
print(f"annotations: {train_model.__annotations__}")





















