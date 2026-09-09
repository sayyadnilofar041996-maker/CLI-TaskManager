from datetime import datetime, date
import json

tasks = []
def load_task():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            loaded_tasks = json.load(file)
    except FileNotFoundError:
        print("No saved tasks found, starting fresh")
        return

    converted_tasks = []
    for task in loaded_tasks:
        task["due_date"] = datetime.strptime(task["due_date"], "%d-%m-%Y").date()
        converted_tasks.append(task)

    tasks = converted_tasks
load_task()

def show_menu():
    print("1. Add Task")
    print("2. Show Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Exit")


def add_task():
    title = input("Enter the task title: ")
    description = input("Enter task description: ")
     
    while True:
        due_date = input("Enter due date ((DD-MM-YYYY)): ")
        try:
            due_date = datetime.strptime(due_date, "%d-%m-%Y").date()
        except ValueError:
            print("Enter date in given format (DD-MM-YYYY)")
            continue
        today = datetime.today().date()
        
        if due_date < today:
            print("Invalid Date !! Please Enter Today Or Future Date")
            continue
        break
            
        
    task = {"title": title, "description": description, "due_date": due_date, "completed": False}
    tasks.append(task)
    save_task()
    print("Task Added Succesfully")

def view_task():
    if tasks == []:
        print("No Task Added Yet")
    else:
        print("Here is the task list")
        for i, task in enumerate(tasks, start =1):
            print("Task",i,":")
            for key,value in task.items():
                print(key, ":", value)


def complete_task():
    try:
        task_number = int(input("Enter the task number: "))
    except ValueError:
        print("Enter the right task number")
        return
    index = task_number - 1
    try:
        task = tasks[index]
        task["completed"] = True
        save_task()
        print("Task mark out completed")
    except IndexError:
        print("No Task with that number")

def delete_task():
    try:
        task_number = int(input("Enter the task number which you want to delete: "))
    except ValueError:
        print("Enter the right task number")
        return    
    index = task_number - 1
    try:
        tasks.pop(index)
        save_task()
        print("Task deleted sucessfully")
    except IndexError:
        print("No Task with that number")


def search_task():
    
    task_title = input("Enter the task title you want to search: ")
   
    found = False
    for task in tasks:
        if task_title.lower() in task["title"].lower():
            print("Title:", task["title"])
            print("Description:", task["description"])
            print("Due Date:", task["due_date"])
            print("Completed:", task["completed"])
            found = True

    if not found:
        print("Task not Found")

def save_task():
    empty_list = []
    for task in tasks:
        task_copy = task.copy()
        task_copy["due_date"] = task["due_date"].strftime("%d-%m-%Y")
        empty_list.append(task_copy)
    with open("tasks.json", "w") as file:
        json.dump(empty_list, file)




def main():
    while True:
        show_menu()
        try:
            choice = int(input("Enter the Menu Number: "))
        except ValueError:
            print("Please Enter an Integer value")
            continue

        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            complete_task()
        elif choice == 4:
            delete_task()
        elif choice == 5:
            search_task()
        elif choice == 6:
            print("Goodbye, See You Soon")
            break
        else:
            print("Invalid Menu Number, Enter Again")

main()

