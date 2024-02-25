while True:
    user_action = input("Type add, edit, complete, show, exit: ").strip()

    match user_action:
        case 'add':
            todo = input("Enter the ToDo: ").title() + "\n"
            file = open('Day6/todos.txt','r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('Day6/todos.txt','w')
            file.writelines(todos)
            file.close()
        case 'edit':
            todo_index = int(input("Enter which ToDo to edit: "))
            todo = input("Enter the ToDo: ").title()
            todos[todo_index-1] = todo
        case 'complete':
            todo_index = int(input("Enter whiich ToDo to complete: "))
            todos.pop(todo_index-1)
        case 'show'|'display':
            file = open('Day6/todos.txt','r')
            todos = file.readlines()
            file.close()

            for index, title in enumerate(todos):
                print(f"{index+1}-{title}")
        case 'exit':
            break
        case _:
            print("You entered an incorrect command! Try again..!")
print('Bye!')
