"""
Description: SavingsAccount class definition extending BankAccount.
Author: {Your Name}
"""

from bank_account import BankAccount


class SavingsAccount(BankAccount):
    """
    Class representing a Savings Account.
    """

    def __init__(self, account_number: str, balance: float, date_created):
        """
        Initializes the SavingsAccount instance.

        :param account_number: The account number of the bank account.
        :param balance: The current balance of the bank account.
        :param date_created: The date the account was created.
        """
        super().__init__(account_number, balance, date_created)

    def get_service_charges(self) -> float:
        """
        Calculates the service charges for the Savings Account.

        :return: The calculated service charges.
        """
        return self.BASE_SERVICE_CHARGE  # Assuming a flat service charge

    def __str__(self):
        """Returns a string representation of the Savings Account."""
        return f"{super().__str__()} Account Type: Savings"
