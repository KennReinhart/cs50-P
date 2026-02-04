# Exceptions
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            # Ask what number is X
            x = int(input(prompt))
        except ValueError:
            # shows err if not INT entered
            print("Integer only, try again")
            # or use pass
        else:
            break
    return x

main()

# and raise


