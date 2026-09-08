from datetime import datetime
def show_menu():
    print("1. Add Task")
    print("2. Show Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Exit")

tasks = []
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
    except IndexError:
        print("No Task with that number")
    


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
            print("Delete Task: Coming Soon")
        elif choice == 5:
            print("Search Task: Coming Soon")
        elif choice == 6:
            print("Goodbye, See You Soon")
            break
        else:
            print("Invalid Menu Number, Enter Again")

main()

