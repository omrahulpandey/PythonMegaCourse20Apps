member = input("Add a member: ").title()

file = open("Day6/files/members.txt",'r')
members = file.readlines()
file.close()

members.append(member + "\n")

with open("Day6/files/members.txt","w") as file:
    file.writelines(members)


