
"""
Description: BankAccount class for the banking system.
Author: [navpreet kaur]
"""

from datetime import date
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number: str, balance: float, date_created: date = None):
        self._account_number = account_number
        self._balance = balance
        
        # Validate date_created or use today's date
        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()

    @abstractmethod
    def get_service_charges(self) -> float:
        pass

    # Getters for attributes if needed
    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def get_date_created(self):
        return self._date_created
