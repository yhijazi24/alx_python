import requests
import sys

def get_employee_info(employee_id):
    try:
        employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
        employee_response.raise_for_status()
        employee_data = employee_response.json()
        employee_name = employee_data['name']
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    try:
        todo_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
        todo_response.raise_for_status()
        todo_data = todo_response.json()
        completed_tasks = [task['title'] for task in todo_data if task['completed']]
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    print(f"{employee_name} is done with tasks ({len(completed_tasks)}/{len(todo_data)}):")
    for task in completed_tasks:
        print(f"\t{task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_info(employee_id)
