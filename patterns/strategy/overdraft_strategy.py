# patterns/strategy/overdraft_strategy.py

from .service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    def __init__(self, overdraft_limit, overdraft_rate):
        """
        Initialize the OverdraftStrategy with an overdraft limit and rate.

        :param overdraft_limit: The maximum amount allowed for overdraft
        :param overdraft_rate: The rate applied to the overdraft balance
        """
        self._overdraft_limit = overdraft_limit  # Protected attribute as per convention
        self._overdraft_rate = overdraft_rate  # Protected attribute as per convention

    def calculate_service_charges(self, account):
        """
        Calculate service charges based on the overdraft balance and rate.

        :param account: The account for which to calculate service charges
        :return: The calculated service charge amount
        """
        # Assuming the account has a 'balance' attribute and an 'overdraft_balance' method
        overdraft_balance = max(0, self._overdraft_limit - account.balance)
        service_charge = overdraft_balance * self._overdraft_rate
        return service_charge
