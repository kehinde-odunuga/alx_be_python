# Develop a script that asks users for a single task, its priority level and if it is time-sensitive.
# The program will then provide a customized reminder for that task, demonstrating control flow and loops without relying on data structures to store multiple tasks.

task = str(input("Enter your task: ")).lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (Yes/No): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print(f"Invalid input. Try again!")