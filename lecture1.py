'''
Conditionals, for example if a happens do this, else do that.
>, >=, <, <=, ==, !=
'''

x = float(input("Enter X: "))
y = float(input("Enter Y: "))

# Bool, true or false
if x < y:
    print("x is smaller than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# Simplified, if we only need to know x is equal to y or vice versa
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")

# Another example, scoring grade
score = float(input("Enter score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Parity, even or odd. Using % (modulo) to find remainder
x = int(input("Enter X: "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# Using function

def main ():
    x = int(input("Enter X: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0
    #return True if n % 2 == 0 else False

main()

# Using match
name = input("Enter name: ").upper()

match name:
    case "A":
        print("A")
    case "B":
        print("B")
    case "C":
        print("C")
    case _:
        print("Unknown")

