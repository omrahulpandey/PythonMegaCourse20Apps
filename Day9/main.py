while True:
    user_action = input("Type add, edit, complete, show, exit: ").strip()
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:].title()

        with open("Day9/todos.txt",'r') as file:
            todos = file.readlines()
        
        todos.append(todo + '\n')

        with open("Day9/todos.txt",'w') as file:
            file.writelines(todos)

    elif 'edit' in user_action:
        todo_index = int(user_action[5:].strip())

        with open("Day9/todos.txt",'r') as file:
            todos = file.readlines()

        todo = input("Enter the ToDo: ").title()
        
        todos[todo_index-1] = todo
        with open("Day9/todos.txt",'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        todo_index = int(user_action[8:].strip())
        with open("Day9/todos.txt",'r') as file:
            todos = file.readlines()

        todos.pop(todo_index -1)
        with open("Day9/todos.txt",'w') as file:
            file.writelines(todos)
            
    elif 'show' in user_action:
        with open("Day9/todos.txt",'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}-{item}")

    elif 'exit' in user_action:
        break

    else :
        print("Invalid keyword, try again!")
    
print("Bye!")