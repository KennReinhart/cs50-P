# OOP, object oriented programming
# tuples, another type of data thats a collection of values,similar to a list but its immutable(unable to be changed).
class Student:
    #instance variables
    def __init__(self, name, house):
        if not name:
            raise ValueError("Student name cannot be empty")

        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} {self.house}"

    # Getter
    def house(self):
        return self.house
    # Setter
    def house(self, house):
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid house name")
        self.house = house #1:24:04

def main():
    # name, house = get_student()
    # print(f"{name} from {house}")
    student = get_student()
    # if student["name"].lower() == "padma":
    #     student["name"] = "Padma"
    #     student["house"] = "Ravenclaw"
    print(student) #(f"{student.name} from {student.house}")

def get_student():
    # using dict is less worrysome to remember which is 0,1 and so forth
    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # -- or --
    # name = input("Name: ")
    # house = input("House: ")
    # return {"name": name, "house": house}

    # name = input("What is your name? ")
    # house = input("What is your house? ")

    #using class
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    #student = Student(name, house) #object, args
    return Student(name, house) #this right here, if [name, house] means lists

if __name__ == "__main__":
    main()

