balance = 100

def cash_with(amount):
    global balance
    print(f"Your balance is {balance}")
    print(f"You are withdrawing {amount}")
    balance -=amount
    print(f"Your new balance is: {balance}")

cash_with()
cash_with()
print(balance)