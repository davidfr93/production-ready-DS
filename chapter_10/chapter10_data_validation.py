import pandas as pd
import numpy as np
# Create sample data with mixed age types
df = pd.DataFrame(
    {
        "customer_id": [1, 2, 3, 4, 5],
        "age": [25, "30", 35, "40", 45], # Some values are strings
        "transaction_amount": [100.00, 50.00, 75.00, 125.00, 200.00],
}
)

print(df)

try:
    young_customers = df[df["age"] < 35]
except TypeError as e:
    print("TypeError:", e)

##########################################################
# Data Validation Made Easy with Pandera
##########################################################

#----------------------------
# Basic Building Blocks
#----------------------------
import pandera.pandas as pa
import pandas as pd

# Create sample data with mixed age types
df = pd.DataFrame(
    {
        "customer_id": [1, 2, 3, 4, 5],
        "age": [25, 30, 35, 40, 45],
        "transaction_amount": [100.0, 50.0, 75.0, 125.0, 200.0],
    }
)

print(df)

# Define the schema
schema = pa.DataFrameSchema(
    {
        "customer_id": pa.Column(
            int, checks=pa.Check.ge(1), unique=True
        ),
        "age": pa.Column(
            int, checks=pa.Check.between(0, 120)
        ),
        "transaction_amount": pa.Column(
            float, checks=pa.Check.ge(0)
        )
    }
)

print(schema)
# Validate the DataFrame
validated_df = schema.validate(df)
print(validated_df)

# Example of validation failure
invalid_df = pd.DataFrame(
    {
        "customer_id": [1, 2, 2, 4, 5],  # Duplicate ID
        "age": [25, 150, -5, 40, 45],  # Invalid ages
        "transaction_amount": [100.00, 50.00, 75.00, 125.00, 200.00],
    }
)
print(invalid_df)

# This will raise SchemaError
try:
    schema.validate(invalid_df)
except pa.errors.SchemaError as err:
    print("SchemaError:", err)

#----------------------------
# Checks
#----------------------------
check_is_even = pa.Check(lambda s: s % 2 == 0)

schema = pa.DataFrameSchema(
    {"column1": pa.Column(int, check_is_even)}
)
schema.validate(pd.DataFrame({"column1": [2, 4, 6, 8]}))

# This will raise SchemaError
try:
    schema.validate(pd.DataFrame({"column1": [2, 4, 6, 7]}))
except pa.errors.SchemaError as err:
    print("SchemaError:", err)



#----------------------------
# Built-in Checks
#----------------------------
from datetime import datetime

customer_schema = pa.DataFrameSchema(
    {
        "customer_id": pa.Column(
            str, checks=pa.Check.str_length(min_value=5)
        ),
        "email": pa.Column(str, checks=pa.Check.str_contains("@")),
        "signup_date": pa.Column(
            datetime, checks=pa.Check.le(datetime.now())
        ),  # Date not in future
    }
)

customer = pd.DataFrame(
    {
        "customer_id": ["CUST01", "CUST02", "CUST03"],
        "email": ["john@mail.com", "jane@mail.com", "bob@mail.com"],
        "signup_date": ["2023-01-01", "2023-02-15", "2023-03-30"],
    }
)
customer.dtypes
customer["signup_date"] = pd.to_datetime(customer["signup_date"])
customer.dtypes
customer

# Validate data
validated_df = customer_schema.validate(customer)
print("Validation passed!")
print(validated_df)



#----------------------------
# Column Check Groups
#----------------------------

# Create sample sales data
df = pd.DataFrame(
	{
		"store": ["NY", "CA", "NY", "CA"],
		"profit": [200.0, 300.0, 300.0, 400.0],
	}
)
df

# Define schema with wide check using groupby
schema = pa.DataFrameSchema(
    {
     "store": pa.Column(str),
     "profit": pa.Column(
         float,
         # Check CA stores have higher average profit than NY
         pa.Check(
             lambda g: g["CA"].mean() > g["NY"].mean(),
             groupby="store",
         ),
     ),   
    }
)

# Define schema with wide check using groupby
schema = pa.DataFrameSchema(
	{
		"store": pa.Column(str),
		"profit": pa.Column(
			float,
			# Check CA stores have higher average profit than NY
			pa.Check(
				lambda g: g["CA"].mean() > g["NY"].mean(),
				groupby="store",
			),
		),
	}
)

# Validate the DataFrame
validated_df = schema.validate(df)
print("Validation passed!")

#----------------------------
# Wide Checks
#----------------------------

# Create sample sales data
df = pd.DataFrame({
    "revenue": [1000.0, 1500.0, 1200.0],
    "expenses": [800.0, 1200.0, 900.0],
    "profit": [200.0, 300.0, 300.0],
})

df

# Define schema with wide check
schema = pa.DataFrameSchema(
    columns={
        "revenue": pa.Column(float),
        "expenses": pa.Column(float),
        "profit": pa.Column(float),
    },
    checks=pa.Check(
        lambda df: df["profit"] == df["revenue"] - df["expenses"]
    ),
)

validated_df = schema.validate(df)
print("Validation passed!")

#----------------------------
# Validation Decorator
#----------------------------

#----------------------------
# Check Input
#----------------------------

from pandera import check_input

input_schema = pa.DataFrameSchema(
    {
        "name": pa.Column(str),
        "age": pa.Column(int, pa.Check.between(0, 120)),
        "score": pa.Column(float, pa.Check.between(0, 100)),
    }
)

@check_input(input_schema)
def calculate_grade(data: pd.DataFrame):
    data["grade"] = pd.cut(
        data["score"],
        bins=[0, 70, 80, 90, 100],
        labels=["F", "C", "B", "A"],
        include_lowest=True,
    )
    return data


df = pd.DataFrame(
    {
        "name": ["John", "Jane", "Bob"],
        "age": [25, 30, 35],
        "score": [95.5, 88.3, 92.7],
    }
)
df

result = calculate_grade(df)
print(result)


invalid_df = pd.DataFrame(
    {
        "name": ["John", "Jane", "Bob"],
        "age": [25, 30, 35],
        "score": [95.5, 88.3, 120.0],
        }
)

invalid_df

try:
    result = calculate_grade(invalid_df)
except pa.errors.SchemaError as err:
    print("SchemaError:", err)


#----------------------------
#  Check Output
#----------------------------
from pandera import check_output

output_schema = pa.DataFrameSchema(
    {
        "name": pa.Column(str),
        "age": pa.Column(int, pa.Check.between(0, 120)),
        "score": pa.Column(float, pa.Check.between(0, 100)),
        "grade": pa.Column(
            str, pa.Check(lambda x: x.isin(["A", "B", "C", "F"]))
        ),
    }
)

@check_input(input_schema)
@check_output(output_schema)
def calculate_grade(data: pd.DataFrame):
    data["grade"] = pd.cut(
        data["score"],
        bins=[0, 70, 80, 90, 100],
        labels=["F", "C", "B", "A"],
        include_lowest=True,
    )
    # Convert category dtype to string dtype
    data["grade"] = data["grade"].astype(str) 
    return data


df = pd.DataFrame(
    {
        "name": ["John", "Jane", "Bob"],
        "age": [25, 30, 35],
        "score": [95.5, 88.3, 92.7],
    }
)
df


result = calculate_grade(df)
print(result)

try:
    result = calculate_grade(df)
except pa.errors.SchemaError as err:
    print("SchemaError:", err)


print(output_schema)

@check_output(output_schema)
def calculate_grade(data: pd.DataFrame):
    data["grade"] = pd.cut(
    data["score"],
    bins=[0, 70, 80, 90, 100],
    labels=["F", "C", "B", "X"],
    include_lowest=True,
    )
    # Convert category dtype to string dtype
    data["grade"] = data["grade"].astype(str) 
    return data

df = pd.DataFrame(
    {
        "name": ["John", "Jane", "Bob"],
        "age": [25, 30, 35],
        "score": [95.5, 88.3, 92.7],
    }
)
df

try:
    result = calculate_grade(df)
except pa.errors.SchemaError as err:
    print("SchemaError:", err)


#----------------------------
# Check Both Inputs and Outputs
#----------------------------
from pandera import check_io

@check_io(data=input_schema, out=output_schema)
def calculate_grade(data: pd.DataFrame):
    data["grade"] = pd.cut(
        data["score"],
        bins=[0, 70, 80, 90, 100],
        labels=["F", "C", "B", "A"],
        include_lowest=True,
    )
    # Convert category dtype to string dtype
    data["grade"] = data["grade"].astype(str) 
    return data


df = pd.DataFrame(
    {
        "name": ["John", "Jane", "Bob"],
        "age": [25, 30, 35],
        "score": [95.5, 88.3, 92.7],
    }
)

df

result = calculate_grade(df)
print(result)


invalid_df = pd.DataFrame(
    {
        "name": ["John", "Jane", "Bob"],
        "age": [25, 30, 35],
        "score": [95.5, 88.3, 120],
        }
)
invalid_df

try:
    result = calculate_grade(invalid_df)
except pa.errors.SchemaError as err:
    print("SchemaError:", err)





#----------------------------
# Other Arguments for Column Validation
#----------------------------

#----------------------------
# Deal with Null Values
#----------------------------
schema = pa.DataFrameSchema(
    {
        "id": pa.Column(int),  # Does not allow nulls
        "name": pa.Column(str, nullable=True),  # Allows nulls
        "age": pa.Column(float, nullable=True),  # Allows nulls
    }
)

df = pd.DataFrame(
	{
		"id": [1, 2, 3],
		"name": ["John", None, "Mary"],
		"age": [25.0, 30.0, None],
	}
)
df

validated_df = schema.validate(df)
print("Validation passed!")


#----------------------------
# Deal with Duplicates
#----------------------------
# Define schema with unique constraint
schema = pa.DataFrameSchema(
    {
        "id": pa.Column(int, unique=True),  # Must be unique
        "name": pa.Column(str),  # Duplicates allowed
    }
)

df = pd.DataFrame(
	{"id": [1, 1, 2], "name": ["John", "Jane", "Mary"]}
)

df

try:
    validated_df = schema.validate(df)
except pa.errors.SchemaError as e:
    print("SchemaError:", e)


#----------------------------
# Required Columns
#----------------------------

# Define schema with required columns
schema = pa.DataFrameSchema(
    {
        "id": pa.Column(int),  # Required column
        "name": pa.Column(str),  # Required column
        "age": pa.Column(int, required=False),  # Optional column
    }
)


df = pd.DataFrame(
	{"id": [1, 2, 3], "name": ["John", "Jane", "Mary"]}
)

df

validated_df = schema.validate(df)
print("Validation passed!")


#----------------------------
# Convert Data Types
#----------------------------
schema = pa.DataFrameSchema(
    {
    "id": pa.Column(int, coerce=True),
    "price": pa.Column(float, coerce=True),
    }
)
print(schema)

df = pd.DataFrame(
    {
        "id": ["12.34", "2", "3"], # Will fail coercion to int
        "price": ["10.99", "20.50", "15.75"],
    }
)

df

try:
    validated_df = schema.validate(df)
except pa.errors.SchemaError as e:
    print("SchemaError:", e)
#----------------------------
# Match Patterns
#----------------------------
# Define schema using regex to match column patterns
schema = pa.DataFrameSchema(
    {
        # Match any column starting with 'score_'
        "score_.*": pa.Column(float, regex=True, nullable=True),
        # Regular columns without regex
        "student_id": pa.Column(int),
        "name": pa.Column(str)
    }
)

print(schema)

df = pd.DataFrame(
    {
        'student_id': [1, 2, 3],
        'name': ['John', 'Mary', 'Bob'],
        'score_math': [85.5, 90.0, None],
        'score_science': [88.0, None, 92.5],
        'score_history': [78.5, 88.5, 95.0],
    }
)

df
validated_df = schema.validate(df)
print("Validation passed!")

#----------------------------
# Schema Model
#----------------------------

# Define the schema using DataFrameSchema
customer_schema = pa.DataFrameSchema(
    {
        "customer_id": pa.Column(
            str,
            checks=pa.Check.str_length(
                min_value=5, max_value=10
            ),
        ),
        "email": pa.Column(
            str, checks=pa.Check.str_contains("@")
        ),
        "signup_date": pa.Column(
            str,
            checks=pa.Check(
                lambda s: pd.to_datetime(s) <= pd.Timestamp.now()
            ),
        ),
    }
)

from pandera.typing import Series

class CustomerSchema(pa.DataFrameModel):
    customer_id: Series[str] = pa.Field(
        str_length={"min_value": 5, "max_value": 10}
    )
    email: Series[str] = pa.Field(str_contains="@")
    signup_date: Series[str]
    
    @pa.check("signup_date")
    def check_date_not_in_future(
        cls, signup_date: Series[str]
    ) -> Series[bool]:
        return pd.to_datetime(signup_date) < pd.Timestamp.now()

# Example data
customer_data = pd.DataFrame(
    {
    "customer_id": ["CUST01", "CUST02"],
    "email": ["john@mail.com", "jane@mail.com"],
    "signup_date": ["2023-01-01", "2023-02-15"],
    }
)


# FIXED: Validate directly using the class
validated_df = CustomerSchema.validate(customer_data)
print("Validation passed!")

# # Validate data
# validated_df = customer_schema.validate(customer_data)
# print("Validation passed!")

from pandera.typing import Series, DataFrame
import hashlib

class CustomerSchema(pa.DataFrameModel):
    customer_id: Series[str] = pa.Field(
        str_length={"min_value": 5, "max_value": 10}
    )
    email: Series[str] = pa.Field(str_contains="@")


class AnonymizedCustomerSchema(pa.DataFrameModel):
    customer_id: Series[str] = pa.Field(
            str_length={"min_value": 5, "max_value": 10}
        )
    anonymized_email: Series[str] = pa.Field(
        str_length={"min_value": 32, "max_value": 32}
    )


@pa.check_types
def anonymize_customer_data(
    df: DataFrame[CustomerSchema],
) -> DataFrame[AnonymizedCustomerSchema]:
    """
    Returns a DataFrame with hashed emails for data privacy
    """
    df = df.copy()
    # Hash email addresses
    df["anonymized_email"] = df["email"].apply(
        lambda x: hashlib.md5(x.encode()).hexdigest()
    )
    # Drop original email column
    df = df.drop("email", axis=1)
    return df
 


anonymized_df = anonymize_customer_data(customer_data)

print(anonymized_df)

#----------------------------
# Export and Load From a YAML File
#----------------------------


#----------------------------
# Export to YAML
#----------------------------
from pathlib import Path
import pandera.pandas as pa

# Define the schema
schema = pa.DataFrameSchema(
    {
        "customer_id": pa.Column(
            int, checks=pa.Check.ge(1), unique=True
        )
    }
)
print(schema)
!ls
# Get a YAML object
print(schema.to_yaml())
yaml_schema = schema.to_yaml()
# Save to a file
f = Path("data/schema.yml")
f.touch()
f.write_text(yaml_schema)

from pathlib import Path
f = Path("data/schema.yml")

with f.open() as file:
    yaml_schema = file.read()


schema = pa.io.from_yaml(yaml_schema)


def analyze_sales_data(sales_df: pd.DataFrame) -> dict:
	# Problems only discovered during processing
	revenue = sales_df["price"] * sales_df["quantity"]

	return {
		"total_revenue": revenue.sum(),
		"max_sale": sales_df["quantity"].max(),
	}


if __name__ == "__main__":
	# Data with issues
	data = pd.DataFrame(
		{
			"price": [50, 100, "invalid", 75],
			"quantity": [5, 3, 2, "error"],
		}
	)
	try:
		results = analyze_sales_data(data)
		print(results)
	except Exception as e:
		print(f"Error during analysis: {e}")


# Define schema for sales DataFrame
sales_schema = pa.DataFrameSchema(
    {
        "price": pa.Column(float, checks=[pa.Check.ge(0)]),
        "quantity": pa.Column(int, checks=[pa.Check.ge(0)]),
    }
)

print(sales_schema)

@check_input(sales_schema)
def analyze_sales_data(sales_df: pd.DataFrame) -> dict:
    revenue = sales_df["price"] * sales_df["quantity"]

    return {
        "total_revenue": revenue.sum(),
        "max_sale": sales_df["quantity"].max(),
    }

data = pd.DataFrame(
    {
        "price": [50, 100, "invalid", 75],
        "quantity": [5, 3, 2, "error"],
    }
)
data

try:
    results = analyze_sales_data(data)
    print(results)
except pa.errors.SchemaError as e:
    print("SchemaError:", e)




#----------------------------
# Validate Only Critical Columns
#----------------------------
# Only validate columns used in the calculation
schema = pa.DataFrameSchema(
	{
		"amount": pa.Column(float, checks=pa.Check.gt(0)),
		"store": pa.Column(
			str, checks=pa.Check.isin(["A", "B"])
		),
	}
)

print(schema)

@pa.check_input(schema)
def get_amount_by_store(df):
	return df.groupby("store")["amount"].sum()


df = pd.DataFrame(
	{
		"customer_id": [1, 2, 3],
		"amount": [100.0, 200.0, 300.0],
		"date": ["2023-01-01", "2023-01-02", "2023-01-03"],
		"store": ["A", "B", "A"],
	}
)
df


amount_by_store = get_amount_by_store(df)

#----------------------------
# THE END
#----------------------------




