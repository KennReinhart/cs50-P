'''
functions (print, etc.)
'''
# Ask user for their name, strip any whitespace and uppercase first char
name = input("What's your name?").strip().title()

# Say hello to user
print("Hello, \"",name,"\"")

# Using format
print(f"Hello, {name}!")

'''
argument
bug, a mistake in a program.
comments, is a note that starts with #
pseudocode, to outline the program in advance
string, sequence of text
parameters
+ - * / %(modulo, divide one number by another )
int, integer
float, decimals
round(number[, ndigits]
'''

# Calculator
# x = int(input("Enter X: "))
# y = int(input("Enter Y: "))
#
# print("X + Y = ",x + y)

# Another way of calc
x = float(input("Enter X: "))
y = float(input("Enter Y: "))

z = round(x + y)

print(f"{z:,}")
'''
This will lead to handling err, what if user doesnt enter number.
'''

# Functions, then we set to value as default
def hello(to="World"):
    print("Hello,", to)

hello()

name = input("What's your name?").strip().title()
hello(name)

# Using main
def main():
    name = input("What's your name?").strip().title()
    hello()
    x = int(input("Enter X: "))
    print("x squarred is", square(x))

def hello():
    print("Hello,", name)

def square(n):
    return n * n or pow(n, 2)

main()

'''
notice that scope is important, because name in main is not the same as name in hello function.
'''
