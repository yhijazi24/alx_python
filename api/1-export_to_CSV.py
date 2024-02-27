#!/usr/bin/python3
import csv
import requests
import sys

def user_info(user_id):
    # API endpoints
    request_user = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    request_todos = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    # Fetching user data
    data_user = requests.get(request_user).json()
    data_todos = requests.get(request_todos).json()

    # Filename for CSV
    filename = f"{user_id}.csv"

    try:
        # Writing to CSV
        with open(filename, "w", newline="") as file:
            csvwriter = csv.writer(file, quoting=csv.QUOTE_ALL)

            # Write CSV header
            csvwriter.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            # Write tasks to CSV
            for task in data_todos:
                csvwriter.writerow([
                    user_id,
                    str(data_user["username"]),
                    task["completed"],
                    task["title"]
                ])

        print(f"Number of tasks in CSV: OK")

    except FileNotFoundError:
        print("CSV file not found.")

# Retrieve user ID from command line argument
user_id = int(sys.argv[1])
user_info(user_id)

