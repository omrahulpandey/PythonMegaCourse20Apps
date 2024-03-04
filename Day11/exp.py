def get_average():
    with open("Day11/data.txt",'r') as file:
        data = file.readlines()

    values = data[1:]
    values = [float(i) for i in values]

    avg_local = sum(values)/len(values)
    return avg_local


average = get_average()
print(average)