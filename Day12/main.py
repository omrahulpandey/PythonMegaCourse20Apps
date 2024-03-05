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
        