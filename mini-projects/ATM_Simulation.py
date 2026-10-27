from decimal import Decimal, InvalidOperation, getcontext

# Two decimal places for currency calculations
getcontext().prec = 28  # good precision; rounding mode default is fine here

class Account:
    def __init__(self):
        self.balance = Decimal("0.00")

    def check_balance(self):
        return f"Your Current Balance is ${self.balance:.2f}"

    def deposit(self, amount_str: str):
        try:
            amt = Decimal(amount_str)
        except InvalidOperation:
            return "Enter Valid Amount"
        if amt <= 0:
            return "Smart ASS🥸 u have to deposit a POSITIVE amount"
        self.balance += amt
        return f"New Balance is ${self.balance:.2f}"

    def withdraw(self, amount_str: str):
        try:
            amt = Decimal(amount_str)
        except InvalidOperation:
            return "Enter Valid Amount"
        if amt <= 0:
            return "Smart ASS🥸 u have to withdraw a POSITIVE amount"
        if amt > self.balance:
            return "Insufficient Funds Moron😂"
        self.balance -= amt
        return f"New Balance is ${self.balance:.2f}"

def main():
    acct = Account()
    print("**********LM Bank Welcomes You**********")
    while True:
        print("*" * 40)
        print("1. Check Balance\n"
              "2. Deposit\n"
              "3. Withdraw\n"
              "4. Exit")
        choice_str = input("What would u like to do today?: ")
        print("*" * 40)

        # Keep your 'match' style; ensure Python 3.10+
        try:
            choice = int(choice_str)
        except ValueError:
            print("Enter Valid Input")
            continue

        match choice:
            case 1:
                print(acct.check_balance())
            case 2:
                amt = input("Enter Amount to be Deposit: ")
                print(acct.deposit(amt))
            case 3:
                amt = input("Enter Amount to be Withdrawn: ")
                print(acct.withdraw(amt))
            case 4:
                print("Thanks for banking with LM Bank. Bye!")
                break
            case _:
                print("Enter Valid Input")

if __name__ == "__main__":
    main()
