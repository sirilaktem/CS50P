name = input("What's your name? ")

# "w" for write | "a" for append
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
