"""
Description: InvestmentAccount class definition extending BankAccount.
Author: {Your Name}
"""

from bank_account import BankAccount
from datetime import date, timedelta


class InvestmentAccount(BankAccount):
    """
    Class representing an Investment Account.
    """

    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, account_number: str, balance: float, date_created, management_fee: float):
        """
        Initializes the InvestmentAccount instance.

        :param account_number: The account number of the bank account.
        :param balance: The current balance of the bank account.
        :param date_created: The date the account was created.
        :param management_fee: The management fee charged for the account.
        """
        super().__init__(account_number, balance, date_created)

        # Validate management fee
        try:
            self.__management_fee = float(management_fee)
        except (ValueError, TypeError):
            self.__management_fee = 2.55

    @property
    def management_fee(self):
        """Returns the management fee."""
        return self.__management_fee

    def get_service_charges(self) -> float:
        """
        Calculates the service charges for the Investment Account.

        :return: The calculated service charges.
        """
        if self.date_created < self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + self.management_fee

    def __str__(self):
        """Returns a string representation of the Investment Account."""
        if self.date_created < self.TEN_YEARS_AGO:
            management_fee_display = "Waived"
        else:
            management_fee_display = f"${self.management_fee:.2f}"

        return f"{super().__str__()}\nDate Created: {self.date_created} Management Fee: {management_fee_display} Account Type: Investment"
