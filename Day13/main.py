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


    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid keyword, please try again!")

