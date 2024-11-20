"""
Description: This module defines the ChequingAccount class, which represents a bank account
that allows overdrafts and applies service charges based on specific strategies.
Author: Navpreet Kaur
Date: 10/09/2024
"""

from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    """
    The ChequingAccount class represents a bank account that allows overdraft protection
    and calculates service charges using the OverdraftStrategy.
    """

    def __init__(self, account_number: str, initial_balance: float, overdraft_limit: float) -> None:
        """
        Initialize the ChequingAccount with an account number, initial balance, and overdraft limit.

        Parameters:
        account_number (str): Unique identifier for the chequing account.
        initial_balance (float): The initial balance of the account.
        overdraft_limit (float): The maximum overdraft amount allowed.
        """
        super().__init__(account_number, initial_balance)  # Initialize the base class
        self._overdraft_strategy = OverdraftStrategy(overdraft_limit)  # Instance of OverdraftStrategy

    def get_service_charges(self) -> float:
        """
        Calculate service charges for the chequing account using the overdraft strategy.

        Returns:
        float: The calculated service charges.
        """
        return self._overdraft_strategy.calculate_service_charges(self.balance)
