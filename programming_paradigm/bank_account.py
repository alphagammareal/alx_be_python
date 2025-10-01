# bank_account.py

class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    # Deposit
    def deposit(self, amount):
        self.account_balance += amount

    # Withdraw
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    # Display Balance
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
