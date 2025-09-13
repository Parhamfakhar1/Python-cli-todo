import json
import os

TODO_FILE = 'tasks.json'

# load tasks
if os.path.exists(TODO_FILE):
    with open(TODO_FILE,'r') as f:
        try:
            tasks = json.load(f)
        except:
            tasks = []
else:
    tasks = []

def save_tasks():
    with open(TODO_FILE,'w') as f:
        json.dump(tasks,f,indent=2)

def show_tasks():
    if not tasks:
        print("No tasks")
        return
    for i, task in enumerate(tasks,1):
        status = '✓' if task['done'] else '✗'
        print(f"{i}. [{status}] {task['task']}")

def add_task():
    t = input("Enter task: ")
    tasks.append({'task':t,'done':False})
    save_tasks()

def mark_done():
    show_tasks()
    try:
        n = int(input("Enter task number to mark done: "))
        if 1 <= n <= len(tasks):
            tasks[n-1]['done']=True
            save_tasks()
        else:
            print("Invalid number")
    except:
        print("Invalid input")

def delete_task():
    show_tasks()
    try:
        n = int(input("Enter task number to delete: "))
        if 1 <= n <= len(tasks):
            tasks.pop(n-1)
            save_tasks()
        else:
            print("Invalid number")
    except:
        print("Invalid input")

def main():
    while True:
        print("\nCLI Todo App")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task Done")
        print("4. Delete Task")
        print("0. Exit")

        choice = input("Enter choice: ")
        if choice=='0':
            print("Exiting...")
            break
        elif choice=='1':
            show_tasks()
        elif choice=='2':
            add_task()
        elif choice=='3':
            mark_done()
        elif choice=='4':
            delete_task()
        else:
            print("Invalid choice")

if __name__=="__main__":
    main()
