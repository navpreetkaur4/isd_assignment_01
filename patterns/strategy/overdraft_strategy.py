# patterns/strategy/overdraft_strategy.py

from .service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Strategy for calculating service charges related to overdrafts.
    """
    
    def __init__(self, overdraft_limit, overdraft_rate):
        """
        Initialize the overdraft strategy with an overdraft limit and rate.
        
        :param overdraft_limit: The overdraft limit for the account.
        :param overdraft_rate: The rate applied to overdraft balance for service charges.
        """
        self._overdraft_limit = overdraft_limit
        self._overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account):
        """
        Calculate service charges based on overdraft usage.
        
        :param account: The account instance for which service charges are being calculated.
        :return: The calculated service charge.
        """
        balance = account.get_balance()  # Assume account has a method to get the balance
        if balance < 0:
            overdraft_amount = min(-balance, self._overdraft_limit)
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE + (overdraft_amount * self._overdraft_rate)
        else:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE
