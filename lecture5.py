# Unit test, it was textCalculator.py and calculator.py combined here.

'''
calculator.py
'''

# pip install pytest, docs.pytest.org
'''
def main():
    x = float(input("What's x?: "))
    print("x squared is", square(x))

def square(x):
    return x * x

if __name__ == "__main__":
    main()
'''

'''
testCalculator.py
'''

# pytest
# pytest testCalucalator.py

'''
import pytest
from calculator import square

# assert, depends on square n+n or n*n, then we categorize
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")
'''

