# #global
# balance = 0
#
# def main():
#     print("Balance:", balance)
#     deposit = int(input("Enter deposit: "))
#     depo(deposit)
#     withdraw = int(input("Enter withdraw: "))
#     cashout(withdraw)
#     print("Balance:", balance)
#
# def depo(n):
#     global balance
#     balance += n
#
# def cashout(n):
#     global balance
#     balance -= n
#
# if __name__ == "__main__":
#     main()

#OOP
class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

#constant
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

def main():
    account = Account()
    print("Balance: ", account.balance)
    account.deposit(100)
    account.withdraw(25)
    print("Balance: ", account.balance)

    cat = Cat()
    cat.meow()

    """
    Docstring, to explain things
    :param n: number of times to n
    :etc
    """
if __name__ == "__main__":
    main()
