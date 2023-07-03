'''
i = 0
while i < 3:
    print("Meow")
    i += 1
'''

'''
for i in range(3):
    print("Meow")
'''

'''
print("Meow\n" * 3, end="")
'''

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("Meow")
