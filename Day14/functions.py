# Functions
def get_todos(path = "Day13/todos.txt"):
    """ Read a text file and returns list of todos 
    from the text file. 
    """
    with open(path,'r') as file:
        todos_local = file.readlines()
        return todos_local


def write_todos(todos_arg, path = "Day13/todos.txt"):
    """ write items in todos to the text file."""
    with open(path,'w') as file:
        file.writelines(todos_arg)

