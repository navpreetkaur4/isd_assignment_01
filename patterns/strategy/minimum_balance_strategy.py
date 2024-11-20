# patterns/strategy/minimum_balance_strategy.py

from .service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    def __init__(self, minimum_balance, penalty_fee):
        """
        Initialize the MinimumBalanceStrategy with a minimum balance and penalty fee.

        :param minimum_balance: The minimum balance required to avoid charges
        :param penalty_fee: The fee applied if balance is below minimum
        """
        self._minimum_balance = minimum_balance  # Protected attribute for internal use
        self._penalty_fee = penalty_fee  # Protected attribute for penalty fee

    def calculate_service_charges(self, account):
        """
        Calculate service charges based on minimum balance requirements.

        :param account: The account for which to calculate service charges
        :return: The calculated service charge amount
        """
        # Assuming the account has a 'balance' attribute
        if account.balance < self._minimum_balance:
            return self._penalty_fee
        return 0  # No charge if balance meets or exceeds minimum
