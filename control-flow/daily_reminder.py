def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            base_message = f"'{task}' is a high priority task"
        case "medium":
            base_message = f"'{task}' is a medium priority task"
        case "low":
            base_message = f"'{task}' is a low priority task"
        case _:
            base_message = f"'{task}' has an unspecified priority"

    if time_bound == "yes":
        reminder = f"Reminder: {base_message} that requires immediate attention today!"
    else:
        if priority in ["high", "medium"]:
            reminder = f"Reminder: {base_message}. Plan accordingly to complete it soon."
        else:
            reminder = f"Note: {base_message}. Consider completing it when you have free time."

    print(reminder)


if __name__ == "__main__":
    main()
