from functions import get_todos, write_todos
while True:
    user_action = input("Type add, edit, complete, show or exit: ")
    
    if user_action.startswith('add'):
        todo = user_action[3:].title()

        todos = get_todos()
        print(help(get_todos))
        todos.append(todo + '\n')

        write_todos(todos)
        print(help(write_todos)) 

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

