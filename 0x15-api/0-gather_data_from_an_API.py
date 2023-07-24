#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
Implemented without recursion
"""
import re
import requests
import sys

API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        employee_id = int(sys.argv[1])

        # Get employee information
        employee_info_url = f"{API}/users/{employee_id}"
        employee_info_response = requests.get(employee_info_url)
        employee_info = employee_info_response.json()
        employee_name = employee_info.get('name')

        # Get TODO list for the employee
        todos_url = f"{API}/todos?userId={employee_id}"
        todos_response = requests.get(todos_url)
        todos = todos_response.json()

        # Filter completed tasks
        completed_tasks = [todo for todo in todos if todo.get('completed')]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todos)

        # Display progress information
        print(f'Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):')
        for task in completed_tasks:
            print(f'\t {task.get("title")}')
    else:
        print("Usage: python script_name.py <employee_id>")

