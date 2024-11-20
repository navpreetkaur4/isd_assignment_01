# patterns/strategy/management_fee_strategy.py

from .service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    # Constant date representing 10 years ago from today
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, management_fee_rate):
        """
        Initialize the ManagementFeeStrategy with a management fee rate.

        :param management_fee_rate: The rate applied for management fees
        """
        self._management_fee_rate = management_fee_rate  # Protected attribute for internal use

    def calculate_service_charges(self, account):
        """
        Calculate service charges based on the management fee rate.

        :param account: The account for which to calculate service charges
        :return: The calculated service charge amount
        """
        # Assuming the account has 'balance' and 'date_created' attributes
        if account.date_created < self.TEN_YEARS_AGO:
            service_charge = account.balance * self._management_fee_rate
        else:
            service_charge = 0  # No charge for accounts created within the last 10 years
        return service_charge
