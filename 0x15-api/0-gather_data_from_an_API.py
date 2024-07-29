#!/usr/bin/python3

""" Python script that, using this REST API, for a given employee ID"""

import requests
import sys

def fetch_employee_todo_list(employee_id):
    # Define the API endpoint
    base_url = 'https://jsonplaceholder.typicode.com'
    
    # Fetch employee data
    user_url = f'{base_url}/users/{employee_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    
    # Fetch TODO list data
    todos_url = f'{base_url}/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    # Extract employee name
    employee_name = user_data['name']
    
    # Extract tasks information
    total_tasks = len(todos_data)
    completed_tasks = [todo['title'] for todo in todos_data if todo['completed']]
    number_of_done_tasks = len(completed_tasks)
    
    # Output the progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py EMPLOYEE_ID")
    else:
        try:
            employee_id = int(sys.argv[1])
            fetch_employee_todo_list(employee_id)
        except ValueError:
            print("Please provide a valid integer for EMPLOYEE_ID")
