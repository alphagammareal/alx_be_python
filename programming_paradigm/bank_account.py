# Create a simple bank account class

class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    # Deposit
    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

    # Withdraw
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return f"Withdrew: ${amount:.2f}"
        elif amount > self.account_balance:
            return "Insufficient funds."

    # display Balnce
    def display_balance(self):
         return f"Current Balance: ${self.account_balance:.2f}" 
