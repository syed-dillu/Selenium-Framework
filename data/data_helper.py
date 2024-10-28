import os
import sys
import pandas as pd
sys.path.append(os.getcwd())
from config.config import *


data = pd.read_excel(get_testdata_url()).to_dict(orient='records')

def get_test_users() -> list:
    """Retrieve a list of test usernames from the data."""
    return [users['UserName'] for users in data]


def get_test_passwords() -> list:
    """Retrieve a list of test passwords from the data."""
    return [password['Password'] for password in data]

def get_test_users_pass() -> list:
    """Retrieve a list of test passwords from the data."""
    return [(user['UserName'],user['Password']) for user in data]

if __name__ == "__main__":
    users = get_test_users()
    passwords = get_test_passwords()
    users_passwords = get_test_users_pass()
    print(f"Users : {users}")
    print(f"Passwords : {passwords}")
    print(f"users and passwords : {users_passwords}")
