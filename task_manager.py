def show_menu():
    print("1. Add Task")
    print("2. Show Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Exit")

def main():
    while True:
        show_menu()
        try:
            choice = int(input("Enter the Menu Number: "))
        except ValueError:
            print("Please Enter an Integer value")

        if choice == 1:
            print("Add Task: Coming Soon")
        elif choice == 2:
            print("Show Task: Coming Soon")
        elif choice == 3:
            print("Complete Taask: Coming Soon")
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
