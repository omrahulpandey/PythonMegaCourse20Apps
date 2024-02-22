todos = []

while True:
    user_action = input("Type add, show, exit: ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a ToDo: ").capitalize()
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                print(item)
        case 'exit':
            break
        case _:
            print("You entered an unknown keyword! Try again.")