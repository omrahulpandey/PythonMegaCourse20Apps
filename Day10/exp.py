try:
    width = float(input("Enter rectange width: "))
    length = float(input("Enter rectange length: "))

    if width==length:
        exit("This looks like a square!")

    area = width*width
    print(area)

except ValueError:
    print("Please enter a number!")