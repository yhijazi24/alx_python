import sys
import requests

def get_employee_info(employee_id):
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    if employee_response.status_code != 200:
        print(f"Error: Could not fetch employee details for ID {employee_id}")
        return

    employee_data = employee_response.json()
    employee_name = employee_data['name']

    todo_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    if todo_response.status_code != 200:
        print(f"Error: Could not fetch TODO list for employee {employee_name}")
        return

    todo_data = todo_response.json()
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task['completed']]
    num_completed_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
