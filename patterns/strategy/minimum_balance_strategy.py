# patterns/strategy/minimum_balance_strategy.py

from .service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Strategy for calculating service charges based on minimum balance requirements.
    """
    
    def __init__(self, minimum_balance, below_minimum_fee, regular_service_charge):
        """
        Initialize the minimum balance strategy with relevant parameters.
        
        :param minimum_balance: The minimum balance required to avoid higher service charges.
        :param below_minimum_fee: The additional fee charged if the balance falls below the minimum.
        :param regular_service_charge: The standard service charge if the balance is above the minimum.
        """
        self._minimum_balance = minimum_balance
        self._below_minimum_fee = below_minimum_fee
        self._regular_service_charge = regular_service_charge

    def calculate_service_charges(self, account):
        """
        Calculate service charges based on whether the account balance meets the minimum requirement.
        
        :param account: The account instance for which service charges are being calculated.
        :return: The calculated service charge.
        """
        balance = account.get_balance()  # Assume account has a method to get the balance
        
        # Check if balance is above or below the minimum
        if balance >= self._minimum_balance:
            return self._regular_service_charge
        else:
            return self._regular_service_charge + self._below_minimum_fee
