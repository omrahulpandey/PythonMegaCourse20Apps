def parse(feet_inches):
    """Parse user input into feet and inches andreturn them."""
    feet = float(feet_inches[0])
    inch = float(feet_inches[1])
    return {"feet":feet, "inch":inch}


def convert(feet, inches):
    """Convert feet and inches into meters and returns it."""
    meters = feet*0.3048 + inches*0.0254
    return meters


feet_inches = input("Enter height in feet and inches: ").split(" ")

parsed = parse(feet_inches)
result = convert(parsed["feet"], parsed["inch"])

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")