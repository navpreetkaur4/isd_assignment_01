# patterns/strategy/management_fee_strategy.py

from datetime import date, timedelta
from .service_charge_strategy import ServiceChargeStrategy

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Strategy for calculating management fee-based service charges.
    """
    
    # Constant representing a date ten years ago from today
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, management_fee_rate, minimum_balance):
        """
        Initialize the management fee strategy with a management fee rate and minimum balance.
        
        :param management_fee_rate: The rate applied for management fees.
        :param minimum_balance: The minimum balance for reduced service charge.
        """
        self._management_fee_rate = management_fee_rate
        self._minimum_balance = minimum_balance

    def calculate_service_charges(self, account):
        """
        Calculate service charges based on management fees and account tenure.
        
        :param account: The account instance for which service charges are being calculated.
        :return: The calculated service charge.
        """
        balance = account.get_balance()  # Assume account has a method to get the balance
        account_age = account.get_account_age()  # Assume account has a method to get age
        
        # Check if account is older than TEN_YEARS_AGO and balance is above minimum
        if account_age < self.TEN_YEARS_AGO and balance >= self._minimum_balance:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE * self._management_fee_rate
        else:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE
