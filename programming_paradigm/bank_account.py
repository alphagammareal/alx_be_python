# Create a simple bank account class

class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    # Deposit
    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount:.2f}")

    # Withdraw
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")

    # Display Balance
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
