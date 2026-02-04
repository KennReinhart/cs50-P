# pip install pytest, docs.pytest.org

def main():
    x = float(input("What's x?: "))
    print("x squared is", square(x))

def square(x):
    return x * x

if __name__ == "__main__":
    main()
