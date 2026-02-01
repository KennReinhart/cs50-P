"""
Loops
"""
# not efficient
print("Meow")
print("Meow")
print("Meow\n")

# use of while loop, i++ and i-- with i+=1 and i-=1
print("While loop")
i = int(input("Enter x times: "))
while i != 0:
    print("Meow")
    i -= 1

# use of for loop and list
print("\nFor loop")
j = int(input("Enter x times: "))
for k in range(j):
    print("Meow")

# validating input
print("\nWhile True")
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n?: "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()

# List. []
upperAlphas = ["A", "B", "C", "D", "E", "F"]
#print(upperAlpha[1])
print("\n")
for upperAlpha in upperAlphas:
    print(upperAlpha)

# len, or length
for i in range(len(upperAlphas)):
    print(i +1, upperAlphas[i])

# Dict, or dictionary. {}
upperAlp = {
    "A": "Aa",
    "B": "Bb",
    "C": "Cc",
}

for alp in upperAlp:
    print(alp, upperAlp[alp], sep=", ")

# Lists of dict. [{}]
otherAlp = [
    {"upper": "A", "lower": "a lowercase", "number": "1"},
    {"upper": "B", "lower": "b lowercase", "number": "2"},
    {"upper": "C", "lower": "c lowercase", "number": "3"},
]

for alp in otherAlp:
    print(alp["upper"], alp["lower"], alp["number"], sep=", ")

# Nested loops
def mario():
    print_square(3)

def print_square(size):
    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # print brick
            print("#", end="")
        # for each row new line
        print()

mario()