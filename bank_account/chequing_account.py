"""
Description: ChequingAccount class definition extending BankAccount.
Author: {navpreet kaur}
"""

from bank_account import BankAccount


class ChequingAccount(BankAccount):
    """
    Class representing a Chequing Account.
    """

    def __init__(self, account_number: str, balance: float, date_created, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the ChequingAccount instance.

        :param account_number: The account number of the bank account.
        :param balance: The current balance of the bank account.
        :param date_created: The date the account was created.
        :param overdraft_limit: The overdraft limit for the account.
        :param overdraft_rate: The overdraft rate for the account.
        """
        super().__init__(account_number, balance, date_created)

        # Validate overdraft limit
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            self.__overdraft_limit = -100.0

        # Validate overdraft rate
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except (ValueError, TypeError):
            self.__overdraft_rate = 0.05

    @property
    def overdraft_limit(self):
        """Returns the overdraft limit."""
        return self.__overdraft_limit

    @property
    def overdraft_rate(self):
        """Returns the overdraft rate."""
        return self.__overdraft_rate

    def get_service_charges(self) -> float:
        """
        Calculates the service charges for the Chequing Account.

        :return: The calculated service charges.
        """
        if self.balance >= self.overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + (self.overdraft_limit - self.balance) * self.overdraft_rate

    def __str__(self):
        """Returns a string representation of the Chequing Account."""
        return f"{super().__str__()}\nOverdraft Limit: ${self.overdraft_limit:.2f} Overdraft Rate: {self.overdraft_rate * 100:.2f}% Account Type: Chequing"
