"""
Description: This file defines the InvestmentAccount class, which represents a investment account with basic operations such as deposit and withdrawal.
Author: Navpreet
Date: 06/10/2024

"""
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    def __init__(self, account_number, balance, management_fee, tenure):
        super().__init__(account_number, balance)
        # Initialize ManagementFeeStrategy with management fee and tenure
        self._management_fee_strategy = ManagementFeeStrategy(management_fee, tenure)

    def get_service_charges(self):
        # Delegate service charge calculation to the ManagementFeeStrategy
        return self._management_fee_strategy.calculate_service_charges(self)
