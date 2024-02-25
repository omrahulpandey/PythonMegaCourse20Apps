filenames = ["a.txt","b.txt","c.txt"]

for file in filenames:
    with open(f"Day6/files/{file}","r") as file:
        print(file.read())