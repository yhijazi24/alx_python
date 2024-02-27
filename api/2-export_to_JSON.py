import requests
import json
import sys

id = sys.argv[1]

request_user = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
request_todos = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}/todos')

data_user = request_user.json()
data_todos = request_todos.json()

sorted_todos = sorted(data_todos, key=lambda x: x['title'])

json_data = {id: []}

for todo in sorted_todos:
    json_data[id].append({
        "task": todo['title'],
        "completed": todo['completed'],
        "username": data_user['username']
    })

json_filename = f'{id}.json'

with open(json_filename, 'w') as jsonfile:
    json.dump(json_data, jsonfile)

print(f'Data exported to {json_filename}')
