class IceCream:
	def __init__(self, flavor: str):
		self.flavor = flavor

	def eat(self):
		print(f"Eating the {self.flavor} ice cream")


chocolate = IceCream("chocolate")
vanilla = IceCream("vanilla")

chocolate.eat()
vanilla.eat()


import numpy as np

class Standardizer:
    def __init__(self, data: np.ndarray) -> None:
        self.data = data
        self.mean = 0
        self.std = 1
        self.is_fitted = False

    def calculate_mean(self) -> None:
        self.mean = np.mean(self.data)

    def calculate_std(self) -> None:
        self.std = np.std(self.data)

    def transform(self) -> np.ndarray:
        return (self.data - self.mean) / self.std


s = Standardizer(np.array([1, 2, 3]))

# Users shouldn't need to call these methods
s.calculate_mean()
s.mean = 10
s.calculate_std()

# Calling transform() will use the wrong mean and std
result = s.transform()
print(f"Unexpected result: {result}")


class Standardizer:
    def __init__(self, data: np.ndarray) -> None:
        self._data = data
    
    def _calculate_mean(self) -> None:
        return np.mean(self._data)
    
    def _calculate_std(self) -> None:
        return np.std(self._data)
    
    def transform(self) -> np.ndarray:
        mean_ = self._calculate_mean()
        std = self._calculate_std()
        return (self._data - mean_) / std

         
s = Standardizer(np.array([1, 2, 3]))
result = s.transform()  # Only expose what users need
print(f"Expected result: {result}")



import pandas as pd

class MissingValueHandler:
	def fill_nulls(self, data: pd.DataFrame) -> pd.DataFrame:
		return data.fillna(data.mean())


class DuplicateHandler:
	def process_dupes(self, data: pd.DataFrame) -> pd.DataFrame:
		return data.drop_duplicates()



def clean_dataset(
	data: pd.DataFrame, cleaners: list
) -> pd.DataFrame:
	for cleaner in cleaners:
		if isinstance(cleaner, MissingValueHandler):
			data = cleaner.fill_nulls(data)
		elif isinstance(cleaner, DuplicateHandler):
			data = cleaner.process_dupes(data)
	return data


class OutlierHandler:
	def process_outliers(
		self, data: pd.DataFrame
	) -> pd.DataFrame:
		mean = data.mean()
		std = data.std()
		z_scores = (data - mean) / std
		return data[z_scores.abs() <= 3]


def clean_dataset(
	data: pd.DataFrame, cleaners: list
) -> pd.DataFrame:
	for cleaner in cleaners:
		if isinstance(cleaner, MissingValueHandler):
			data = cleaner.fill_nulls(data)
		elif isinstance(cleaner, DuplicateHandler):
			data = cleaner.process_dupes(data)
		# Add new cleaner types here
		elif isinstance(cleaner, OutlierHandler):
			data = cleaner.process_outliers(data)
	return data






from abc import ABC, abstractmethod
import pandas as pd
from typing import List

class DataTransformer(ABC):
    @abstractmethod
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """Transform the input data"""
        pass

class MissingValueHandler(DataTransformer):
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.fillna(data.mean())    

class DuplicateRemover(DataTransformer):
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.drop_duplicates()

def clean_dataset(
    data: pd.DataFrame, transformers: List[DataTransformer]
) -> pd.DataFrame:
    for transformer in transformers:
        data = transformer.transform(data)
    return data


if __name__ == "__main__":
    df = pd.DataFrame({"values": [1, 2, None, 2]})
    print(df)
    transformers = [MissingValueHandler(), DuplicateRemover()]
    clean_df = clean_dataset(df, transformers)
    print(clean_df)



import pandas as pd
from sklearn.preprocessing import StandardScaler


class MissingValueHandler:
    def process(self, df: pd.DataFrame) -> pd.DataFrame:
        print("Handle missing values")
        return df.fillna(0)


class FeatureScaler(MissingValueHandler):
    def process(self, df: pd.DataFrame) -> pd.DataFrame:
        df = super().process(df)
        print("Scale numeric features")
        scaler = StandardScaler().set_output(transform="pandas")
        return scaler.fit_transform(df)


class NumericDataProcessor(FeatureScaler):
    def process(self, df: pd.DataFrame) -> pd.DataFrame:
        df = super().process(df)
        print("Remove duplicates")
        return df.drop_duplicates()

df = pd.DataFrame(
	{
		"feature1": [10.5, np.nan, 10.5],
		"feature2": [100.0, 200.0, 100.0],
	}
)

print(df)

processor = NumericDataProcessor()
result = processor.process(df)
print("Result:\n", result)


import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from typing import List

class DataPipeline:
    def __init__(self, steps: List[callable]):
        self.steps = steps
    
    def process(self, df: pd.DataFrame) -> pd.DataFrame:
        for step in self.steps:
            df = step(df)
        return df



def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    print("Handle missing values")
    return df.fillna(0)

def scale_features(df: pd.DataFrame) -> pd.DataFrame:
    print("Scale numeric features")
    scaler = StandardScaler().set_output(transform="pandas")
    return scaler.fit_transform(df)
    
def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    print("Remove duplicates")
    return df.drop_duplicates()

df = pd.DataFrame(
	{
		"feature1": [10.5, np.nan, 10.5],
		"feature2": [100.0, 200.0, 100.0],
	}
)

print(df)

# Pipeline without scaling
pipeline = DataPipeline(
    [handle_missing_values, remove_duplicates]
)
result = pipeline.process(df)
print(result)

# Advanced Class Toolkit
class ModelMetrics:
    def __init__(self, model_name: str):
          self.model_name = model_name
    
    def __str__(self) -> str:
        return f"{self.model_name} Performance"
    
    def __repr__(self) -> str:
        return f"ModelMetrics(model_name='{self.model_name}')"


rf_metrics = ModelMetrics("Random Forest")
print(rf_metrics)
rf_metrics
print(repr(rf_metrics))


class ExperimentResults:
    def __init__(self, learning_rate, val_loss):
          self.learning_rate = learning_rate
          self.val_loss = val_loss
    
    def __eq__(self, other):
        """Check if experiments are similar"""
        return (
            abs(self.val_loss - other.val_loss) < 0.01
            and abs(self.learning_rate - other.learning_rate)
            < 1e-4
        )
    
    def __add__(self, other):
        """Average results of multiple experiment runs"""
        return ExperimentResults(
            (self.learning_rate + other.learning_rate) / 2,
            (self.val_loss + other.val_loss) / 2,
        )

exp1 = ExperimentResults(learning_rate=0.001, val_loss=0.245)
exp2 = ExperimentResults(learning_rate=0.001, val_loss=0.248)

print("Comparisons:")
print(f"exp1 == exp2: {exp1 == exp2}")

# Average experiments
avg_exp = exp1 + exp2
print(f"\nAverage loss: {avg_exp.val_loss:.3f}")
print(f"LR: {avg_exp.learning_rate}")


# Data Classes
from dataclasses import dataclass

@dataclass
class ModelMetrics:
    model_name: str
    accuracy: int

rf_metrics = ModelMetrics("Random Forest", 0.945)
print(rf_metrics)


# Data Classes
from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    name: str
    grades: List[int] = field(default_factory=list)


student1 = Student("John")
student2 = Student("Jane")

# Appending grade to student1
student1.grades.append(90)
print(student1)

# doesn't affect the grades of student2
print(student2)

# Pydantic
from pydantic import BaseModel, Field, ValidationError
from typing import List

class DatasetConfig(BaseModel):
    dataset_name: str
    features: List[str]
    target_column: str
    train_split: float = Field(gt=0, lt=1)



# Using the model in a machine learning pipeline
config = DatasetConfig(
    dataset_name="housing_prices",
    features=["sqft", "bedrooms", "location"],
    target_column="price",
    train_split=0.8,
)

# This will raise a validation error
try:
    invalid_config = DatasetConfig(
        dataset_name="housing_prices",
        features=["sqft", "bedrooms", "location"],
        target_column="price",
        train_split=1.5,
    )
except ValidationError as e:
    print("ValidationError:", e)



# Classmethod in Python
import pandas as pd

# Create sample DataFrame for housing data
housing_df = pd.DataFrame(
    {
        "price": [250000, 350000, 450000],
        "area": [1500, 2000, 2500],
        "bedrooms": [2, 3, 4],
    }
)
print(housing_df)

# Save to CSV
housing_df.to_csv("data/housing.csv", index=False)

import pandas as pd
from typing import List

class Dataset:
    def __init__(
        self, data: pd.DataFrame, name: str, features: List[str]
    ):
        self.data = data
        self.name = name
        self.features = features
    
    def __str__(self) -> str:
        return (
            f"Dataset '{self.name}' with {len(self.features)} "
            f"features and {len(self.data)} samples"
        )
    
    @classmethod
    def from_csv(cls, filepath: str) -> "Dataset":
        data = pd.read_csv(filepath)
        name = filepath.split("/")[-1].replace(".csv", "")
        features = list(data.columns)
        return cls(data, name, features)
	
		
housing_data = Dataset.from_csv("data/housing.csv")
print(housing_data)

# Staticmethod
import numpy as np

class ModelEvaluator:
    def __init__(self, predictions: np.ndarray, actuals: np.ndarray):
         self.predictions = predictions
         self.actuals = actuals
    
    @staticmethod
    def is_valid_probability(predictions: np.ndarray) -> bool:
        """Check if predictions are valid probabilities"""
        return all(0 <= p <= 1 for p in predictions)
    
    def calculate_metrics(self) -> dict:
        """Instance method using static methods"""
        if not self.is_valid_probability(self.predictions):
            raise ValueError("Invalid prediction probabilities")
        squared_errors = (self.predictions - self.actuals) ** 2
        rmse = np.sqrt(np.mean(squared_errors))
        return {"rmse": round(rmse, 3)}
        

# Using static methods directly without instance
predictions = np.array([0.1, 0.8, 0.3])
# predictions = np.array([0.1, -0.8, 0.3])
actuals = np.array([0, 1, 0])

is_valid_probabilities = ModelEvaluator.is_valid_probability(
    predictions
)
print(f"Valid probabilities: {is_valid_probabilities}")

checking_proba = ModelEvaluator(predictions, actuals)
checking_proba.is_valid_probability(predictions)


# Property Decorator
import pandas as pd
from typing import Optional

class DatasetProfile:
    def __init__(self, data: pd.DataFrame):
        self._data = data
        self._sample_size: Optional[int] = None
    
    @property
    def sample_size(self) -> Optional[int]:
        """Getter for sample size"""
        return self._sample_size
    
    @sample_size.setter
    def sample_size(self, value: int) -> None:
        """Setter with validation"""
        if not isinstance(value, int):
            raise TypeError("Sample size must be an integer")
        if value <= 0 or value > len(self._data):
            raise ValueError("Invalid sample size")
        self._sample_size = value


df = pd.DataFrame({"A": [1, 2, None, 4], "B": [5, None, 7, 8]})
print(df)
profile = DatasetProfile(df)

# Using setter with validation
try:
    profile.sample_size = 2
    print(f"Sample size set to: {profile.sample_size}")
    
    # This will raise an error
    profile.sample_size = -1
except ValueError as e:
    print(f"ValueError: {e}")


#############################################################
# Slots in Python Classes
#############################################################
from typing import List, Optional
import sys

class StandardFeature:
    def __init__(self, name: str, values: List[float]):
        self.name = name
        self.values = values
        
class OptimizedFeature:
    __slots__ = ["name", "values"]
    
    def __init__(self, name: str, values: List[float]):
        self.name = name
        self.values = values


values = [1, 2, 3, 4, 5]
values

# Standard class (without slots)
std_feature = StandardFeature("age", values)

# Dynamic attribute creation works
std_feature.new_attr = "allowed"

# Optimized class (with slots)
opt_feature = OptimizedFeature("age", values)

# Dynamic attribute creation is not allowed
try:
    opt_feature.new_attr = "not allowed"
except AttributeError as e:
    print(
        f"AttributeError: Cannot add new attributes to slotted class"
    )

# Memory comparison
print(f"Memory without slots: {sys.getsizeof(std_feature)} bytes")
print(f"Memory with slots: {sys.getsizeof(opt_feature)} bytes")


#############################################################
# Scikit-Learn Compatible Class
#############################################################
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
from typing import Optional

class OutlierCapper(BaseEstimator, TransformerMixin):
    def __init__(self, percentile: float = 95):
        self.percentile = percentile
        self.threshold_: Optional[np.ndarray] = None
    
    def fit(self, X: np.ndarray, y: Optional[np.ndarray] = None):
        self.threshold_ = np.percentile(X, self.percentile, axis=0)
        return self
    
    def transform(self, X: np.ndarray) -> np.ndarray:
        if self.threshold_ is None:
            raise ValueError("Fit the transformer first")
        return np.minimum(X, self.threshold_)


X = np.array([[1, 10], [2, 20], [100, 1000]])
X


pipeline = Pipeline(
    [
        ("capper", OutlierCapper(percentile=75)),
        ("scaler", StandardScaler()),
    ]
)


X_transformed = pipeline.fit_transform(X)
print("Transformed data:\n", X_transformed)


























