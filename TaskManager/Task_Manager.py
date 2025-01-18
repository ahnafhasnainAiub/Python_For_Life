
import json

def load_data():   
    try:
        with open('taskmanager.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def data_helper(tasks):
    with open('taskmanager.txt', 'w') as file:
        json.dump(tasks, file)


def show_all(tasks):
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. ")

def add_task(tasks):
    name = input("Enter Task name: ")
    time = input("Enter Task time: ")

    tasks.append({'name': name, 'time': time})
    data_helper(tasks)

def update_task(tasks):
    pass

def delete_task(tasks):
    pass

def main():
    tasks = load_data()

    while True:
        print("Welcome to the Task Manager App | Choose an option")
        print("Enter 1 for Show all the task")
        print("Enter 2 for Add a new task")
        print("Enter 3 for Update task")
        print("Enter 4 for Delete task")
        print("Enter 5 for Exit")
        choice = input("Please enter a value: ")

        print(tasks)

        match choice:
            case '1':
                show_all(tasks)
            case '2':
                add_task(tasks)
            case '3':
                update_task(tasks)
            case '4':
                delete_task(tasks)
            case '5':
                break
            case _:
                print("Invalid Input")



if __name__ == "__main__":
    main()