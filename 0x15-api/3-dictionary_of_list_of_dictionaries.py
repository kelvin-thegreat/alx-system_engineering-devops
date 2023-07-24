#!/usr/bin/python3
"""
API - https://jsonplaceholder.typicode.com
gathers data from API and exports it to JSON file
Implemented using recursion
"""
import json
import requests

API = "https://jsonplaceholder.typicode.com"
"""REST API url"""


def get_employee_todo_data(employee_id):
    """
    Get employee's TODO list data.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: List of TODO items owned by the employee.
    """
    todos_url = f"{API}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url).json()
    return todos_response


def export_all_employees_todo_to_json():
    """
    Export TODO data for all employees to a JSON file.

    Returns:
        None
    """
    all_employee_data = {}

    users_response = requests.get(f"{API}/users").json()

    for user in users_response:
        user_id = user.get('id')
        username = user.get('username')
        todos = get_employee_todo_data(user_id)

        user_data = []
        for todo in todos:
            task_title = todo.get("title")
            completed_status = todo.get("completed")
            user_data.append({"username": username, "task": task_title, "completed": completed_status})

        all_employee_data[str(user_id)] = user_data

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(all_employee_data, json_file)


if __name__ == '__main__':
    export_all_employees_todo_to_json()

