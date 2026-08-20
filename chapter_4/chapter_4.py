# Numbers
age = 25

# Strings
name = "Alice"

# Lists
fruits = ["apple", "banana", "orange"]

# Dictionaries
student = {"name": "Bob", "age": 20, "grades": [85, 90, 88]}

# Sets
unique_numbers = {1, 2, 3, 4, 5}

# Tuples
coordinates = (10, 20)



# List of daily temperatures
temperatures = [72.5, 73.1, 71.8, 74.2, 73.5]

# Add a new temperature
temperatures.append(72.9)

# Access temperature by position
print(f"Temperature on day 3: {temperatures[2]}°F")

# Modify a temperature
temperatures[0] = 73.0


# Tuple of coordinates
point = (10, 20)

# Can't modify coordinates
try:
    point[0] = 15
except TypeError as e:
    print(f"Error: {e}")


# Can be used as a dictionary key
points = {
    (10, 20): "Point A",
    (30, 40): "Point B",
}

# Set of unique visitors
visitors = {"user1", "user2", "user3"}

# Add a new visitor
visitors.add("user4")

# Check if a user has visited
print(f"Has user1 visited?: {'user1' in visitors}")

# Remove duplicates from a list
all_visits = ["user1", "user2", "user1", "user3", "user2"]
unique_visitors = set(all_visits)
print(f"Unique visitors: {unique_visitors}")



user = {
    "name": "John",
    "age": 30,
    "email": "john@example.com"
}

# Access information by key
print(f"User's name: {user['name']}")

# Update information
user["age"] = 31

# Add new information
user["location"] = "New York"


import pandas as pd

# Problematic use of reserved keywords
class = pd.read_csv('data/classes.csv')

import pandas as pd
class_df = pd.read_csv('data/classes.csv')


def calculate_loan_payment(principal, years):
    num_payments = years * 12
    if principal > 1_000_000:
        return "Loan amount too high"
    if years > 30:
        return "Term too long"
    return (
        principal
        * (0.01 * (1 + 0.01) ** num_payments)
        / ((1 + 0.01) ** num_payments - 1)
    )

MONTHLY_INTEREST_RATE = 0.01
GROWTH_FACTOR = 1 + MONTHLY_INTEREST_RATE
MAX_LOAN_AMOUNT = 1_000_000
MAX_LOAN_TERM = 30
def calculate_loan_payment(principal, years):
    num_payments = years * 12
    if principal > MAX_LOAN_AMOUNT:
        return "Loan amount too high"
    if years > MAX_LOAN_TERM:
        return "Term too long"
    return (
    principal
    * (MONTHLY_INTEREST_RATE * GROWTH_FACTOR**num_payments)
    / (GROWTH_FACTOR**num_payments - 1)
    )


# Problematic use of singular nouns for collections
city = ['New York', 'London', 'Tokyo', 'Paris', 'Sydney']

if city == 'New York':
    # This won't work as expected if city is a list
    print("Big Apple!")

# Improved code using plural nouns for collections
cities = ['New York', 'London', 'Tokyo', 'Paris', 'Sydney']

if 'New York' in cities:
    print("Big Apple!")

prices = [5, 3, 5, 4, 5, 3, 3.5, 3]
price_diff = sum(prices[:4]) - sum(prices[4:])
print(price_diff)


prices = [5, 3, 5, 4, 5, 3, 3.5, 3]

# Create slice objects to represent specific ranges
JANUARY = slice(0, 4) # First 4 elements
FEBRUARY = slice(4, len(prices)) # Remaining elements

price_diff = sum(prices[JANUARY]) - sum(prices[FEBRUARY])
print(f"Price difference between January and February: {price_diff}")



import os
full_path = '/home/user/data/project/data.csv'

# Split the path into directory and filename
directory, filename = os.path.split(full_path)

# Add a new file to directory
new_file_name = 'new_data.csv'
new_file_path = os.path.join(directory, new_file_name)
print(new_file_path)

import os
full_path = '/home/user/data/project/data.csv'

# Split the path into directory and filename
directory, _ = os.path.split(full_path)

# Add a new file to directory
new_file_name = 'new_data.csv'

new_file_path = os.path.join(directory, new_file_name)
print(new_file_path)




class Bank:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

# Bad: Accessing the balance directly from outside the class
bank_account = Bank("123456789", 200)
print(f"Initial balance: {bank_account.balance}")

# Bad: Modifying the balance directly from outside the class
bank_account.balance += 500
print(f"Balance after deposit: {bank_account.balance}")


class Bank:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self._balance = initial_balance # Private variable
    
    def get_balance(self):
        return self._balance
        
bank_account = Bank("123456789", 200)
print(f"Initial balance: {bank_account.get_balance()}")



import pandas as pd
# Problematic code with variable repurposing
df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
df

df = df.assign(c=lambda x: x["a"] + x["b"]) # has a new column
df

df = df[df["c"] > 5] # df now has filtered rows
df

df = df.drop("b", axis=1) # df now has different columns
df
# What's in df now? It's hard to tell without checking each step


import pandas as pd
# Improved code with distinct variables
original_df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
original_df

df_with_sum = original_df.assign(c=lambda x: x["a"] + x["b"])
df_with_sum

filtered_df = df_with_sum[df_with_sum["c"] > 5]
filtered_df

final_df = filtered_df.drop("b", axis=1)
final_df











