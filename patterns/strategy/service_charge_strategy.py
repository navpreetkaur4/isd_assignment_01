# patterns/strategy/service_charge_strategy.py

from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    # Define any shared constants here if they apply across multiple strategies.
    MINIMUM_BALANCE_FEE = 5.00  # Example constant; adjust or add more if needed

    @abstractmethod
    def calculate_service_charges(self, account):
        """
        Abstract method for calculating service charges for a given account.
        This will be implemented by subclasses to apply specific service charge strategies.

        :param account: The account for which to calculate service charges
        :return: The calculated service charge amount
        """
        pass
