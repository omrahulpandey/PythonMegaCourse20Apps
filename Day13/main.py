def get_todos(path_arg):
    with open(path_arg,'r') as file:
        todos_local = file.readlines()
        return todos_local


def write_todos(path_arg, todos_arg):
    with open(path,'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, edit, complete, show or exit: ")

    path = "Day13/todos.txt"

    if user_action.startswith('add'):
        todo = user_action[3:].title()

        todos = get_todos(path)
        todos.append(todo + '\n')

        write_todos(path, todos)

    elif user_action.startswith('show'):
        todos = get_todos(path)
        for index, item in enumerate(todos):
            print(f"{index+1}.{item.strip()}")

    elif user_action.startswith('edit'):
        try:
            todo_index = int(user_action[5:].strip())

            todos = get_todos(path)

            todo = input("Enter the ToDo: ").strip().title()

            todos[todo_index-1] = todo + '\n'

            write_todos(path, todos)
        except:
            print("Invlaid input, try again.")

    elif user_action.startswith('complete'):
        try:
            todo_index = int(user_action[8:].strip())

            todos = get_todos(path)
            todos.pop(todo_index-1)

            write_todos(path, todos)
        except:
            print("Invaid input, try again.")
            
    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid keyword, please try again!")

