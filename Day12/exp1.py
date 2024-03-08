feet_inches = input("Enter fee and inches: ")

def convert(feet_inches):
    parts = feet_inches.split(' ')
    feet = parts[0]
    inches = parts[1]

    meters  = fee*0.3048 + inches*0.0254

result = convert(feet_inches)

print(f"{result} is the converted value")