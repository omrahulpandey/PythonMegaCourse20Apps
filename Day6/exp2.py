filenames = ['doc.txt','report.txt','presentation.txt']

for file in filenames:
    with open(f"Day6/files/{file}","w") as file:
        file.write("Hello")
