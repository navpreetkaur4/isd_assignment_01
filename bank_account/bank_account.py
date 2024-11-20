"""
Description: This module defines the BankAccount class, which represents a bank account with basic operations such as deposit and withdrawal.
Author: Navpreet Kaur
Date: 10/09/2024
"""

from abc import ABC
from patterns.observer.subject import Subject

class BankAccount(Subject, ABC):
    """
    The BankAccount class represents a bank account that can notify its observers
    of significant changes, such as low balance warnings or large transactions.
    """

    # Define constants for the bank account class
    LOW_BALANCE_LEVEL: float = 50.00  # Example low balance threshold
    LARGE_TRANSACTION_THRESHOLD: float = 1000.00  # Example threshold for large transactions

    def __init__(self, account_number: str, initial_balance: float) -> None:
        """
        Initialize the BankAccount with an account number and an initial balance.

        Parameters:
        account_number (str): Unique identifier for the bank account.
        initial_balance (float): The initial balance of the account.
        """
        super().__init__()  # Call to the superclass __init__ to initialize the observers list
        self.account_number: str = account_number
        self.balance: float = initial_balance

    def update_balance(self, amount: float) -> None:
        """
        Update the balance of the bank account by adding the specified amount.
        Notify observers if the balance is below the LOW_BALANCE_LEVEL
        or if the transaction amount exceeds the LARGE_TRANSACTION_THRESHOLD.

        Parameters:
        amount (float): The amount to add to the balance. Can be negative for withdrawals.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")

        self.balance += amount  # Update the balance

        # Check for low balance warning
        if self.balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning ${self.balance:.2f}: on account {self.account_number}.")

        # Check for large transaction warning
        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction ${amount:.2f}: on account {self.account_number}.")
