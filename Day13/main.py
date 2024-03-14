def get_todos(path = "Day13/todos.txt"):
    """ Read a text file and returns list of todos 
    from the text file. 
    """
    with open(path,'r') as file:
        todos_local = file.readlines()
        return todos_local


def write_todos(todos_arg, path = "Day13/todos.txt"):
    """ write items in todos to the text file."""
    with open(path,'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, edit, complete, show or exit: ")
    
    if user_action.startswith('add'):
        todo = user_action[3:].title()

        todos = get_todos()
        print(help(get_todos)) #prints docstring
        todos.append(todo + '\n')

        write_todos(todos)
        print(help(write_todos))  # prints docstring

    elif user_action.startswith('show'):
        todos = get_todos()
        for index, item in enumerate(todos):
            print(f"{index+1}.{item.strip()}")

    elif user_action.startswith('edit'):
        try:
            todo_index = int(user_action[5:].strip())

            todos = get_todos()

            todo = input("Enter the ToDo: ").strip().title()

            todos[todo_index-1] = todo + '\n'

            write_todos(todos)
        except:
            print("Invlaid input, try again.")

    elif user_action.startswith('complete'):
        try:
            todo_index = int(user_action[8:].strip())

            todos = get_todos()
            todos.pop(todo_index-1)

            write_todos(todos)
        except:
            print("Invaid input, try again.")

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid keyword, please try again!")

