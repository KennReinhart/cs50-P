# OOP, object oriented programming
# tuples, another type of data thats a collection of values,similar to a list but its immutable(unable to be changed).

def main():
    # name, house = get_student()
    # print(f"{name} from {house}")
    student = get_student()
    if student["name"].lower() == "padma":
        student["name"] = "Padma"
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_student():
    # using dict is less worrysome to remember which is 0,1 and so forth
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    # -- or --
    # name = input("Name: ")
    # house = input("House: ")
    # return {"name": name, "house": house}

    # name = input("What is your name? ")
    # house = input("What is your house? ")
    return student #this right here, if [name, house] means lists

if __name__ == "__main__":
    main()

