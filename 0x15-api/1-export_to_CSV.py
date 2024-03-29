#!/usr/bin/python3
"""
API - https://jsonplaceholder.typicode.com
gathers data from API and exports it to CSV file
"""
import re
import requests
import sys


API = "https://jsonplaceholder.typicode.com"
"""REST API Link"""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_response = requests.get('{}/users/{}'.format(API, id)).json()
            todos_response = requests.get('{}/todos'.format(API)).json()
            user_name = user_response.get('username')
            todos = list(filter(lambda x: x.get('userId') == id, todos_response))
            with open('{}.csv'.format(id), 'w') as file:
                for todo in todos:
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            id,
                            user_name,
                            todo.get('completed'),
                            todo.get('title')
                        )
                    )
