import pandas as pd
import numpy as np
import logging

# def process_sales_data(filepath: str) -> pd.DataFrame:
#     try:
#         df = pd.read_csv(filepath)
#         total_sales = df['sales'].sum()
#         daily_average = df.groupby('date')['sales'].mean()
#         return df
#     except Exception as e:
#         print(f"Error processing data: {e}")


# def process_sales_data(filepath: str) -> pd.DataFrame:
#     try:
#         df = pd.read_csv(filepath)
#         total_sales = df['sales'].sum()
#         daily_average = df.groupby('date')['sales'].mean()
#         return df
#     except FileNotFoundError:
#         logging.error(f"File '{filepath} not found")
#     except pd.errors.EmptyDataError:
#         logging.error(f"File '{filepath}' is empty")
#     except KeyError:
#         logging.error("Column 'sales' is not found")
#     except Exception as e:
#         logging.error(f"Unexpected error: {e}")

# if __name__ == "__main__":
#     result = process_sales_data("data/sales_data.csv")
    



# nums = [1, 2, "3"]

# try:
#     sum_nums = sum(nums)
#     mean_nums = sum_nums / len(nums)
#     print(f"The mean of the numbers is {mean_nums}.")
# except TypeError as e:
#     raise TypeError("Items in the list must be numbers") from e


nums = [1, 2, "3"]
try:
    sum_nums = sum(nums)
except TypeError as e:
    raise TypeError("Items in the list must be numbers") from e
else:
    mean_nums = sum_nums / len(nums)
    print(f"The mean of the numbers is {mean_nums}.")
    