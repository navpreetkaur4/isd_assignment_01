# patterns/strategy/service_charge_strategy.py

from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    """
    Base class for service charge strategies, using the Strategy Pattern.
    """
    # Define any necessary constants that were previously in the BankAccount class
    BASE_SERVICE_CHARGE = 5.00  # Example base charge, adjust if needed

    @abstractmethod
    def calculate_service_charges(self, account):
        """
        Calculate service charges based on the specific strategy.
        This method must be implemented by all subclasses.
        """
        pass
