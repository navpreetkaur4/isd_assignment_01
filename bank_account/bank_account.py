
"""
Description: BankAccount class for the banking system.
Author: [Your Name]
"""

class BankAccount:
    def __init__(self, account_number: int, client_number: int, balance: float = 0.0):
        """
        Initializes a new BankAccount instance with validated attributes.

        :param account_number: An integer representing the bank account number.
        :param client_number: An integer representing the client number.
        :param balance: A float representing the initial balance.
        :raises ValueError: If validations fail.
        """
        # Validate account_number
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        self.__account_number = account_number

        # Validate client_number
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        # Validate balance
        try:
            self.__balance = float(balance)
        except (ValueError, TypeError):
            self.__balance = 0.0

    @property
    def account_number(self) -> int:
        """Gets the account number."""
        return self.__account_number

    @property
    def client_number(self) -> int:
        """Gets the client number."""
        return self.__client_number

    @property
    def balance(self) -> float:
        """Gets the current balance."""
        return self.__balance

    def update_balance(self, amount: float):
        """
        Updates the account balance by adding the specified amount.

        :param amount: The amount to add (can be negative).
        """
        try:
            amount = float(amount)
            self.__balance += amount
        except (ValueError, TypeError):
            pass  # Invalid amount, do not update balance

    def deposit(self, amount: float):
        """
        Deposits a specified amount into the account.

        :param amount: The amount to deposit (must be positive and numeric).
        :raises ValueError: If amount is not numeric or not positive.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:.2f} must be positive.")
        self.update_balance(amount)

    def withdraw(self, amount: float):
        """
        Withdraws a specified amount from the account.

        :param amount: The amount to withdraw (must be positive, numeric, and not exceed balance).
        :raises ValueError: If amount is not numeric, not positive, or exceeds balance.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Withdrawal amount: ${amount:.2f} must be positive.")
        if amount > self.__balance:
            raise ValueError(f"Withdrawal amount: ${amount:.2f} must not exceed the account balance: ${self.__balance:.2f}.")
        self.update_balance(-amount)

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the BankAccount.

        :return: Formatted string.
        """
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:.2f}\n"
