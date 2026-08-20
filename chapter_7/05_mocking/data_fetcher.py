"""
Simple function for mocking demonstration from Chapter 7.
This matches the example shown in the book.
"""

import pandas as pd

def get_active_users():
    # Direct database dependency
    df = pd.read_sql(
        "SELECT user_id FROM users WHERE status = 'active'", 
        "postgresql://user:pass@localhost:5432/prod"
    )
    return df.head(10)



# def fetch_user_data(user_id):
#     """Fetch user data by ID - for testing purposes."""
#     # This would normally connect to a database
#     # For demo purposes, return sample data
#     return {"user_id": user_id, "name": f"User {user_id}", "active": True}


# def get_user_count():
#     """Get total user count - for testing purposes."""
#     # This would normally query the database
#     return 42