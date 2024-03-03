while True:
    user_action = input("Type add, edit, complete, show or exit: ").strip()

    if user_action.startswith('add'):  
        todo = user_action[4:].title()

        with open("Day10/todos.txt",'r') as file:
            todos = file.readlines()
    
        todos.append(todo + '\n')

        with open("Day10/todos.txt",'w') as file:
            file.writelines(todos)
        

    elif user_action.startswith('edit'):
        try:    
            todo_index = int(user_action[5:])
            todo = input("Enter the todo: ").title()

            with open("Day10/todos.txt",'r') as file:
                todos = file.readlines()

            todos[todo_index-1] = todo + '\n'

            with open("Day10/todos.txt",'w') as file:
                file.writelines(todos)

        except (ValueError, IndexError):
            print("Incorrect input, try again!")
            continue

    elif user_action.startswith('complete'):
        try:   
            todo_index = int(user_action[8:])

            with open("Day10/todos.txt",'r') as file:
                todos = file.readlines()

            todos.pop(todo_index-1)

            with open("Day10/todos.txt",'w') as file:
                file.writelines(todos)
        
        except (ValueError, IndexError):
            print("Incorrect input, try again!")
            continue

    elif user_action.startswith('show'):
        with open("Day10/todos.txt",'r') as file:
            todos = file.readlines()
        
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}.{item}")

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid keyword! Try again.")

print("Bye")