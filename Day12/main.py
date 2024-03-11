def get_todos(filepath):
    with open(filepath,'r') as file:
        todos_local = file.readlines()
    return todos_local


def put_todos(filepath, todos_arg):
    with open(filepath,'w') as file:
                file.writelines(todos_arg)


while True:
    user_action = input("Type add, edit, complete, show or exit: ").strip()
    path = "Day12/todos.txt"
    if user_action.startswith('add'):
        try:
            todo = user_action[4:].title()
            todos = get_todos(path)
            todos.append(todo + '\n')

            put_todos(path,todos)

        except (ValueError,IndexError):
            print(f"{user_action} is an invalid command. Try again")
            continue

    elif user_action.startswith('edit'):
        try:
            todo_index = int(user_action[5:])
            todo = input("Enter ToDo to edit:  ").title()

            todos = get_todos(path)
            todos[todo_index-1] = todo + '\n'

            put_todos(path,todos)

        except (ValueError, IndexError):
            print(f"{user_action} is an invalid ommand. Try again")
            continue
    
    elif user_action.startswith('complete'):
        try:
            todo_index = int(user_action[9:])
            todos = get_todos(path)

            todos.pop(todo_index-1)
            
            put_todos(path,todos)
        except (ValueError, IndexError):
            print(f"{user_action} is an invalid command. Try again")
            continue

    elif user_action.startswith('show'):
        try:
            todos = get_todos(path)

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index+1}.{item}")

        except (ValueError,IndexError):
            print(f"{user_action} is an invalid command. Try again")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print(f"{user_action} is an invalid keyword. Try again!")
        