def get_nr_items(string):
    items = string.split(",")
    return len(items)
    
user_input = input("Enter the string: ")
print(get_nr_items(user_input))