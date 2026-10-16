
tasks = []

while True:
    print("\nadd / view / complete / exit")
    command = input("Enter command: ")

    if command == "add":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif command == "view":
        if tasks == []:
            print("No tasks found.")
        else:
            for i in range(len(tasks)):
                print(i + 1, tasks[i])

    elif command == "complete":
        if tasks == []:
            print("No tasks found.")
        else:
            for i in range(len(tasks)):
                print(i + 1, tasks[i])

            try:
                number = int(input("Enter task number: "))

                if number >= 1 and number <= len(tasks):
                    tasks[number - 1] = "Completed: " + tasks[number - 1]
                    print("Task completed!")

                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif command == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid command.")