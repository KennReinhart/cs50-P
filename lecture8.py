# OOP, object oriented programming
# tuples, another type of data thats a collection of values,similar to a list but its immutable(unable to be changed).

def main():
    # name, house = get_student()
    # print(f"{name} from {house}")
    student = get_student()
    if student[0] == "Padma" or "padma":
        student[0] = "Padma"
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("What is your name? ")
    house = input("What is your house? ")
    return [name, house] #this right here, if [] means lists

if __name__ == "__main__":
    main()
