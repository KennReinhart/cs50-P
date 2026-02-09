import csv

students = []

with open("students.csv") as file:
    '''
    #only read csv
    reader = csv.reader(file)
    for row in reader:
        # manually
        # students.append({"name": name, "home": home})
        # all at one
        students.append(row)
    '''
    # read as dictionary
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

# checking the students lists
# print(students)

for student in sorted(students, key=lambda student: student["house"]):
    print(f"{student['name']} is from {student['house']}")

# csv dictwriter
name = input("What is your name? ")
house = input("What is your house? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, house])
