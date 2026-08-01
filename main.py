from todo_management import ToDoList

todo = ToDoList()

while True:
    print("Welcome to your personal TodoList!")
    print(f'1. Show Tasks \n2. Add a Task \n3.Remove a Task \n4. Save Tasks \n5. Load Tasks \n6.Exit \n')
    print("Enter your choice:")
    choice = int(input())

    match choice:
        case 1:
            todo.show_tasks()

        case 2:
            print("Add your task with name , description and priority")
            name = input("name: ")
            description = input("description: ")
            priority = input("priority: ")
            todo.add_task(name, description, priority)

        case 3:
            name = input("Write name of task for removing : ")
            todo.remove_task(name)

        case 4:
            todo.save_to_csv()
            print("Saved to file.")

        case 5:
            print("Loaded!")
            todo.load_from_csv()

        case 6:
            print("Exiting...")
            break

        case _ :
            print("Invalid! \n Choose another number.")