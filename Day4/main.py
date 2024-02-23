# List indexing and tuples
todos = []

while True:
    user_action = input("Type add, edit, show, exit: ").strip()

    match user_action:
        case 'add':
            todo = input('Enter a ToDo: ').title()
            todos.append(todo)
        case 'edit':
            number = int(input("Enter which ToDo to edit: "))
            number = number-1
            todo = input("Enter a ToDo: ").title()
            todos[number] = todo
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break
        case _:
            print("You have entered incorrect value. Try again!")

print("Bye!")