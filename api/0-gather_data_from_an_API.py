#!/usr/bin/python3
"""a Python script using a rest api"""
import requests
import sys

""" Functions for gathering  data from an API """

def fetch_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch employee data
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data["name"]

    # Fetch TODO list data
    response = requests.get(todos_url)
    todos = response.json()

    return employee_name, todos

def display_todo_progress(employee_name, todos):
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo["completed"]]
    num_completed_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print("\t", task["title"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    employee_name, todos = fetch_employee_data(employee_id)
    display_todo_progress(employee_name, todos)
