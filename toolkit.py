
# My Personal Mini-Toolkit

print("================================")
print(" Welcome to My Personal Toolkit!")
print("================================")

while True:
    print("\n===== MY PERSONAL MINI-TOOLKIT =====")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Multiplication Table")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

# Tool 1: This calculator allows users to add, subtract,
# multiply, and divide two numbers.

    if choice == "1":
        # Tool 1: Simple Calculator
        print("\n--- Simple Calculator ---")

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")

            operation = input("Choose an operation (1-4): ")

            if operation == "1":
                result = num1 + num2
                print(f"Result: {result}")

            elif operation == "2":
                result = num1 - num2
                print(f"Result: {result}")

            elif operation == "3":
                result = num1 * num2
                print(f"Result: {result}")

            elif operation == "4":
                if num2 != 0:
                    result = num1 / num2
                    print(f"Result: {result}")
                else:
                    print("Sorry, you cannot divide by zero.")

            else:
                print("Invalid operation.")

        except ValueError:
            print("Please enter valid numbers.")

# Tool 2: This tool allows users to add, view, and remove
# tasks from a to-do list using a Python list.

    elif choice == "2":
        # Tool 2: To-Do List
        tasks = []

        while True:
            print("\n--- TO-DO LIST ---")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Return to main menu")

            task_choice = input("Choose an option (1-4): ")

            if task_choice == "1":
                task = input("Enter your task: ")
                tasks.append(task)
                print(f"Task '{task}' added successfully!")

            elif task_choice == "2":
                if len(tasks) == 0:
                    print("Your to-do list is empty.")
                else:
                    print("\nYour tasks:")
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

            elif task_choice == "3":
                if len(tasks) == 0:
                    print("There are no tasks to remove.")
                else:
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

                    try:
                        task_number = int(input("Enter the task number to remove: "))

                        if 1 <= task_number <= len(tasks):
                            removed = tasks.pop(task_number - 1)
                            print(f"Task '{removed}' removed successfully!")
                        else:
                            print("Invalid task number.")

                    except ValueError:
                        print("Please enter a valid number.")

            elif task_choice == "4":
                break

            else:
                print("Invalid choice. Please try again.")

# Tool 3: This tool displays the multiplication table
# of a number entered by the user using a for loop.

    elif choice == "3":
        # Tool 3: Multiplication Table
        print("\n--- MULTIPLICATION TABLE ---")

        try:
            number = int(input("Enter a number: "))
            print(f"\nMultiplication table for {number}:")

            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")

        except ValueError:
            print("Please enter a valid whole number.")

    elif choice == "4":
        print("Thank you for using my toolkit. Goodbye!")
        break

    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please try again.")
