#global
balance = 0

def main():
    print("Balance:", balance)
    deposit = int(input("Enter deposit: "))
    depo(deposit)
    withdraw = int(input("Enter withdraw: "))
    cashout(withdraw)
    print("Balance:", balance)

def depo(n):
    global balance
    balance += n

def cashout(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()