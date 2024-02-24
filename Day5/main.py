todos = []

while True:
    user_action = input("Type add, edit, complete, show, exit: ").strip()

    match user_action:
        case 'add':
            todo = input("Enter ToDo to be added: ").title()
            todos.append(todo)
        case 'edit':
            todo_index = int(input("Enter which ToDo to edit: "))
            todo = input("Enter ToDo to be added: ").title()
            todos[todo_index-1] = todo
        case 'show'|'display':
            for index, item in enumerate(todos):
                row = f"{index+1}-{item}"
                print(row)
        case 'complete':
            todo_index = int(input("Enter which ToDo to complete: "))
            todos.pop(todo_index -1)
        case 'exit':
            break
        case _:
            print("Enter correct keyword, again!")

print("Bye!")
