class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance, default is 0."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount from the account if funds are sufficient."""
        if amount > self.__account_balance:
            return False  # Insufficient funds
        elif amount > 0:
            self.__account_balance -= amount
            return True
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Display the current account balance in a user-friendly format."""
        print("Current Balance:" ,self.__account_balance)
