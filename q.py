def deposit(balance):
    x = int(input("How much would you like to deposit? "))
    print("Deposit is " + str(x))
    new_balance = balance + x
    print("Your balance is: " + str(new_balance))
    return new_balance

def withdraw(balance):
    y = int(input("How much would you like to withdraw? "))
    if y > balance:
        print("Insufficient balance.")
    else:
        r = balance - y
        print("Total balance after withdrawal: " + str(r))
        return r

def bank():
    balance = 0
    balance = deposit(balance)
    balance = withdraw(balance)

bank()
