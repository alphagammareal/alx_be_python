#  Prompt for a Single Task:
task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

#  Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high" | "medium" |"low":
        if time_bound == "yes":
            print(f"Remainder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    
    case _:
        print("Invalid input")