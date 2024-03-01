password = input('Enter a password: ')

if len(password) > 7:
    print("Great password there")
if len(password) == 7:
    print("Password is OK, but not too strong")
if len(password) <=7:
    print("Your password is weak")
