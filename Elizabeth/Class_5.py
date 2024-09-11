

# Class: BankAccount
class BankAccount:
    # Attributes: account_number, balance
    def __init__(self, account_number, balance):
        # Initialize attributes
        self.account_number = account_number
        self.balance = balance

    # Method: deposit()
    def deposit(self, amount):
        # Add the deposit amount to the balance
        self.balance += amount

    # Method: withdraw()
    def withdraw(self, amount):
        # Subtract the withdrawal amount from the balance if there are sufficient funds
        if amount <= self.balance:
            self.balance -= amount
        else:
            # Print an error message if there are insufficient funds
            print("Insufficient funds")