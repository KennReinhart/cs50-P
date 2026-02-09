'''File I/O, input output'''
# lists
names = [] #empty lists
students = []

for _ in range(3):
    # name = input("Enter name: ")
    names.append(input("Enter name: "))

for name in sorted(names):
    file = open("names.txt", "a")
    file.write(f"{name}\n")
    file.close()
    # print(f"Hello, {name}")

# directly from list, using with
with open("names.txt", "a") as file:
    file.write(f"{names}\n")

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

# sorted
for name in sorted(names, reverse=True):
    print(f"hello, {name}")

#or we can do it like this
# with open("names.txt") as file:
#     for line in sorted(file, reverse=True):
#         print("hello, ", line.rstrip())

# csv, comma separated
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # print(f"{name} is in {house}")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]
def get_house(student):
    return student["house"]

# or use of lambda, key=lambda student: student["name"]
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']}, {student['house']}")