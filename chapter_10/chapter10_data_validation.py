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
































