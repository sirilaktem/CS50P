'''
students = ["Hermione", "Harry", "Ron"]
'''

'''
for student in students:
    print(student)
'''

'''
for i in range(len(students)):
    print(i + 1, students[i])
'''

'''
students = {"Hermione": "Gryffindor",
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin"
            }

for student in students:
    print(student, students[student], sep=", ")
'''

'''
    name        house       patronus
0   Hermione    Gryffindor  Otter
1   Harry       Gryffindor  Stag
2   Ron         Gryffindor  Jack Russell terrier
3   Draco       Slytherin
'''

students = [
    {
        "name": "Hermione",
        "house": "Gryffindor",
        "patronus": "Otter"
    },
    {
        "name": "Harry",
        "house": "Gryffindor",
        "patronus": "Stag"
    },
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronus": "Jack Russell terrier"
    },
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronus": None
    }
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
