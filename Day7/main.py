while True:
    user_input = input("Type add, edit, show, complete, exit: ").strip()

    match user_input:
        case 'add':
            todo = input("Enter the Todo task: ").title()
            file = open('Day7/todos.txt','r')
            todos = file.readlines()
            file.close()

            todos.append(todo + '\n')

            with open('Day7/todos.txt','w') as file:
                file.writelines(todos)
                
        case 'edit':
            todo_index = int(input("Enter the ToDo to edit: "))
            todo = input("Enter the ToDo task: ").title()

            file = open('Day7/todos.txt','r')
            todos = file.readlines()
            file.close()

            todos[todo_index-1] = todo

            with open('Day7/todos.txt','w') as file:
                file.writelines(todos)

        case 'complete':
            todo_index = int(input("Enter the ToDo to complete: "))
            file = open('Day7/todos.txt','r')
            todos = file.readlines()
            todos.pop(todo_index-1)

            with open('Day7/todos.txt','w') as file:
                file.writelines(todos)

        case 'show'|'display':
            file = open('Day7/todos.txt','r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index+1}-{item}")
        case 'exit':
            break
        case _:
            print(f"{user_input} is an unknown keyword. Try again!")
print('Bye!')