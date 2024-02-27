import csv
import requests
import sys

id = sys.argv[1]

request_user = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
request_todos = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}/todos')

data_user = request_user.json()
data_todos = request_todos.json()

sorted_todos = sorted(data_todos, key=lambda x: x['title'])

completed_tasks = sum(1 for todo in sorted_todos if todo['completed'])

csv_filename = f'{id}.csv'

with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

    for todo in sorted_todos:
        csv_writer.writerow([id, data_user['username'], todo['completed'], todo['title']])

print(f'Data exported to {csv_filename}')
