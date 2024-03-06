def get_todos():
    with open("Day11/todos.txt",'r') as file:
        todos = file.readlines()
    return todos


while True:
    user_action = input("Type add, edit, complete, show or exit: ").strip()

    if user_action.startswith('add'):
        try:
            todo = user_action[4:].title()
            todos = get_todos()
            todos.append(todo + '\n')
        except (ValueError,IndexError):
            print(f"{user_action} is an invalid command. Try again")
            continue

    elif user_action.startswith('edit'):
        try:
            todo_index = int(user_action[5:])
            todo = input("Enter ToDo to edit:  ")

            todos = get_todos()
            todos[todo_index-1] = todo
        except (ValueError, IndexError):
            print(f"{user_action} is an invalid ommand. Try again")
            continue
    
    elif user_action.startswith('complete'):
        try:
            pass
        except (ValueError, IndexError):
            print(f"{user_action} is an invalid command. Try again")
            continue

    elif




