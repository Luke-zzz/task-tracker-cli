import argparse
import os,json
from datetime import datetime

TASKS_FILE='tasks.json'

def load_task():
    if os.path.exists(TASKS_FILE):
        try:
            with open('tasks.json', 'r') as outfile:
                data = json.load(outfile)
                return data
        except json.JSONDecodeError:
            return {}
    return {}

def save_task(data):
    with open('tasks.json', 'w') as outfile:
        json.dump(data, outfile, default=str)
        outfile.close()

def add_task(description):
    tasks = load_task()
    task_id = str(len(tasks)+1)
    tasks[task_id] = {"description": description,"status": "todo","created_at":datetime.now(),"updated_at":datetime.now()}
    save_task(tasks)
    print("Task added successfully")

def update_task(task_id, description):
    tasks = load_task()
    if task_id in tasks:
        tasks[task_id]["description"] = description
        save_task(tasks)
        print("Task updated successfully")
    else:
        print(f"Task ID {task_id} not found")

def list_task():
    tasks = load_task()
    if tasks=={}:
        print("No tasks found.")
    for task_id, task in tasks.items():
        print(f"{task_id}: {task['description']}\t [{task['status']}]\t {task['created_at']}")


def delete_task(task_id):
    tasks = load_task()
    if task_id in tasks:
        del tasks[task_id]
        save_task(tasks)
        print("Task deleted successfully")
    else:
        print(f"Task ID {task_id} not found")

def mark_task(task_id,status):
    tasks = load_task()
    if task_id in tasks:
        tasks[task_id]["status"] = status
        save_task(tasks)
        print("Task marked successfully")
    else:
        print(f"Task ID {task_id} not found")


def clear_task():
    save_task({})
    print("Task cleared successfully")

def list_done():
    tasks = load_task()
    if tasks=={}:
        print("No tasks found.")
    else:
        for task_id, task in tasks.items():
            if task["status"] == "done":
                print(f"{task_id}: {task['description']}\t [{task['status']}]\t {task['created_at']}")


def list_in_progress():
    tasks = load_task()
    if tasks == {}:
        print("No tasks found.")
    else:
        for task_id, task in tasks.items():
            if task["status"] == "in-progress":
                print(f"{task_id}: {task['description']}\t [{task['status']}]\t {task['created_at']}")



def main():
    print("Welcome to Task Tracker! Type 'exit' to stop.")

    while True:
        user_input = input("")
        if user_input == "exit":
            print("Thank you for using Task Tracker!")
            break
        commands = user_input.split(" ")
        title = commands[0]
        if title != "task-cli":
            print("Invalid command. Please try again.")
            continue



        if title == "task-cli":
            try:
                command = commands[1]
                if len(commands)==2:
                    if command == "list":
                        list_task()
                    elif command == "clear":
                        clear_task()
                else:
                    if command == "add":
                        description = commands[2:]
                        add_task(" ".join(description))
                    elif command == "list":
                        sub_description = commands[3]
                        if sub_description == "done":
                            list_done()
                        elif sub_description == "in-progress":
                            list_in_progress()
                    elif command == "delete":
                        description = commands[2]
                        delete_task(description)
                    elif command == "mark-in-progress":
                        description = commands[2]
                        mark_task(description,"in-progress")
                    elif command == "mark-done":
                        description = commands[2]
                        mark_task(description,"done")
                    elif command == "update":
                        sub_description = commands[3:]
                        description = commands[2]
                        update_task(description," ".join(sub_description))
            except Exception as e:
                print("Invalid command. Please try again.")
                continue



if __name__ == '__main__':
    main()
