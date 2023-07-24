#!/usr/bin/python3
"""
Returns info about employee TODO progress.
"""

import re
import requests
import sys

API = "https://jsonplaceholder.typicode.com"

def get_employee_todo_progress(employee_id):
    """
    Get employee TODO progress and display it.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Get employee information
    employee_info_url = f"{API}/users/{employee_id}"
    employee_info_response = requests.get(employee_info_url)
    employee_info = employee_info_response.json()
    EMPLOYEE_NAME = employee_info.get('name')

    # Get TODO list for the employee
    todos_url = f"{API}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Filter completed tasks
    completed_tasks = [todo for todo in todos if todo.get('completed')]
    NUMBER_OF_DONE_TASKS = len(completed_tasks)
    TOTAL_NUMBER_OF_TASKS = len(todos)

    # Display progress information
    print(f'Employee {EMPLOYEE_NAME} is done with tasks ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
    for task in completed_tasks:
        TASK_TITLE = task.get("title")
        print(f'\t {TASK_TITLE}')

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        EMPLOYEE_ID = int(sys.argv[1])
        get_employee_todo_progress(EMPLOYEE_ID)
    else:
        print("Usage: python script_name.py <employee_id>")

