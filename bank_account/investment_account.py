"""
Description: This file defines the InvestmentAccount class, which represents a investment account with basic operations such as deposit and withdrawal.
Author: Navpreet
Date: 06/10/2024

"""

from patterns.strategy.management_fee_strategy import ManagementFeeStrategy
from bank_account import BankAccount

class InvestmentAccount(BankAccount):
    def __init__(self, account_number, balance, management_fee, service_charge):
        super().__init__(account_number, balance)
        # Initialize the strategy with appropriate arguments
        self._service_charge_strategy = ManagementFeeStrategy(
            management_fee=management_fee,
            service_charge=service_charge
        )
    
    def get_service_charges(self):
        # Call to calculate service charges using the strategy
        return self._service_charge_strategy.calculate_service_charges(self)
