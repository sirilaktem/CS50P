''' Write a file
name = input("What's your name? ")

# "w" for write | "a" for append
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
'''

# Read exsiting file using "r" for read mode
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
