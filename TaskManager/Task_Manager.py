
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
    print("\n")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['name']}, Duration : {task['time']}.")
       

def add_task(tasks):
    name = input("Enter Task name: ")
    time = input("Enter Task time: ")

    tasks.append({'name': name, 'time': time})
    data_helper(tasks)

def update_task(tasks):
    show_all(tasks)
    index = int(input("Enter the task number : "))
    if 1<= index <= len(tasks):
        name = input("Enter Task name: ")
        time = input("Enter the task duaration: ")
        tasks[index-1] = {'name':name, 'time': time}
        data_helper(tasks)
    else:
        print("Invalid Task Number")

def delete_task(tasks):  
    show_all(tasks)
    index = int(input("Enter the task number that you wants to delete: "))
    
    if 1<= index <= len(tasks):
        del tasks[index -1]
        data_helper(tasks)
        print(f"Task number {index} is Succesfully Deleted")
    else:
        print("Invalid task number provided")

def main():
    tasks = load_data()

    while True:
        print("\n Welcome to the Task Manager App | Choose an option")
        print("Enter 1 for Show all the task")
        print("Enter 2 for Add a new task")
        print("Enter 3 for Update task")
        print("Enter 4 for Delete task")
        print("Enter 5 for Exit")
        choice = input("Please enter a value: ")

        # print(tasks)

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