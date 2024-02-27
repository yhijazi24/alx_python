import requests
import csv
import sys

id = sys.argv[1]

request_user = requests.get('https://jsonplaceholder.typicode.com/users/' + id)
request_todos = requests.get('https://jsonplaceholder.typicode.com/users/' + id + '/todos')

data_user = request_user.json()
data_todos = request_todos.json()

completed_tasks = []

for item in data_todos:
    completed_tasks.append([data_user.get('id'), data_user.get('name'), item.get('completed'), item.get('title')])

csv_filename = id + '.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
    csv_writer.writerows(completed_tasks)

print(f'Data exported to {csv_filename}')
