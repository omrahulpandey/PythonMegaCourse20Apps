while True:
    user_action = input("Type add, edit, complete, show, exit: ")

    match user_action:
        case 'add':
            todo = input("Enter the ToDo: ").title()
            with open('Day8/todos.txt','r') as file:
                todos = file.readlines()

            todos.append(todo + '\n')

            with open('Day8/todos.txt','w') as file:
                file.writelines(todos)

        case 'edit':
            todo_index = int(input("Enter the ToDo to edit: "))
            todo = input("Enter the ToDo: ").title()
            with open('Day8/todos.txt','r') as file:
                todos = file.readlines()

            todos[todo_index-1] = todo + '\n'

            with open('Day8/todos.txt','w') as file:
                file.writelines(todos)
    
        case 'complete':
            todo_index = int(input("Enter the ToDo to complete: "))
            with open('Day8/todos.txt','r') as file:
                todos = file.readlines()

            todo_to_remove = todos[todo_index-1].strip('\n')
            todos.pop(todo_index-1)

            with open('Day8/todos.txt','w') as file:
                file.writelines(todos)

            print(f"ToDo {todo_to_remove} was removed from the list.")

        case 'show'|'display':
            with open('Day8/todos.txt','r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index+1}-{item}")
        case 'exit':
            break
        case _:
            print(f"{user_action} is an invalid keyword. Try again!")
print("Bye!")
