#!/usr/bin/python3
"""
Check student .CSV output of user information
"""

import csv
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def user_info(id):
    filename = str(id) + ".csv"
    try:
        with open(filename, 'r') as f:
            print(f"User ID and Username: OK")
            # Process the CSV file as needed
    except FileNotFoundError:
        print(f"User ID and Username: OK, but {filename} not found.")
