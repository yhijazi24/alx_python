import sys
import requests
import csv

def get_employee_data(employee_id):
    # Fetching employee details
    employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetching employee's TODO list
    todo_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todos = todo_response.json()

    # Counting completed tasks
    completed_tasks = [task for task in todos if task['completed']]

    return employee_name, completed_tasks, todos

def export_to_csv(employee_name, completed_tasks, all_tasks):
    filename = f"{employee_name.replace(' ', '_')}_todo.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in all_tasks:
            completed_status = "True" if task["completed"] else "False"
            writer.writerow([task["userId"], employee_name, completed_status, task["title"]])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    employee_name, completed_tasks, all_tasks = get_employee_data(employee_id)

    # Displaying employee TODO list progress
    total_tasks = len(all_tasks)
    num_completed_tasks = len(completed_tasks)
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

    # Exporting to CSV
    export_to_csv(employee_name, completed_tasks, all_tasks)
    print(f"Data exported to {employee_name.replace(' ', '_')}_todo.csv")
