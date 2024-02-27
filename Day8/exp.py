
date = input("Enter today's date: ").strip()
mood = input("How do you rate your mood from 1 to 10?: ")
thought = input("Let your thought's flow:\n").capitalize()

with open(f"Day8/journal/{date}.txt",'w') as file:
    file.writelines(mood + '\n')
    file.write(thought)
