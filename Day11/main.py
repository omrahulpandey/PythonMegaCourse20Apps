def get_todos():
    with open("Day11/todos.txt",'r') as file:
        todos = file.readlines()
    return todos


def put_todos(todos):
    with open("Day11/todos.txt",'w') as file:
        file.writelines(todos)


while True:
    user_action = input("Type add, edit, complete, show or exit: ").strip()
    if user_action.startswith('add'):
        todo = user_action[4:].title()

        todos = get_todos()

        todos.append(todo + '\n')

        put_todos(todos)

    elif user_action.startswith('edit'):
        try:
            todo_index = int(user_action[5:])

            todo = input("Enter the ToDO to edit: ").title()

            todos = get_todos()
            
            todos[todo_index-1] = todo + '\n'

            put_todos(todos)
        
        except (ValueError, IndexError):
            print(f"{user_action} is Invalid command, please try again!")
            continue

    elif user_action.startswith('complete'):
        try:
            todo_index = int(user_action[9:])

            todos = get_todos()
            
            todos.pop(todo_index-1)

            put_todos(todos)

        except (ValueError, IndexError):
            print(f"{user_action} is Invalid command, please try again")

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}.{item}")
    
    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid keyword, Pleasetry again!")

print("Bye!")
    
