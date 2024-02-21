tasks = {}
completed = []
def add_task():
    while True:
        print("Add a new task")
        task = input("Enter name: ")
        desc = input("Descriptions: ")
        tasks[task]=desc
        msg = input("Do you want to continue?(yes/no): ")
        if msg == 'no':
            break

def mark():
    print("Enter a name of the task: ")
    task_name = input('>>> ')
    if task_name in tasks:
        if task_name not in completed:
            completed.append(task_name)
            print(f"{task_name} has been marked as completed!")
        else:
            print(f"{task_name} is already completed!")
    else:
        print(f"{task_name} is not defined!")

    print("Completed tasks:")
    for t in completed:
        print(t)
def view():
    for t,d in tasks.items():
        print(f"Name: {t} - {d}")

def remove_task():
    task = input("Enter a task name: ")
    if task in tasks:
        del tasks[task]
        print(f"{task} is deleted!")
    else:
        print(f"{task} is not define!")

def menu():
    while True:
        print("Welcome to To Do list!")
        print(f"Choose: " 
              f"\n1 - To add a new task "
              f"\n2 - To view tasks "
              f"\n3 - To mark tasks "
              f"\n4 - To remove a task "
              f"\n5 - Exit")
        javob = int(input(">>> "))
        try:
            if javob == 1:
                add_task()
            elif javob == 2:
                view()
            elif javob == 3:
                mark()
            elif javob == 4:
                remove_task()
            elif javob == 5:
                break
        except ValueError:
            print("Please enter a number!")

menu()