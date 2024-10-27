"""
Description: This module defines the SavingsAccount class, which extends the BankAccount class.
Author: Sukhtab Singh Warya
Date: 06/10/2024
"""

from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy
from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, minimum_balance, below_minimum_fee, regular_service_charge):
        super().__init__(account_number, balance)
        # Initialize the strategy with appropriate arguments
        self._service_charge_strategy = MinimumBalanceStrategy(
            minimum_balance=minimum_balance,
            below_minimum_fee=below_minimum_fee,
            regular_service_charge=regular_service_charge
        )
    
    def get_service_charges(self):
        # Call to calculate service charges using the strategy
        return self._service_charge_strategy.calculate_service_charges(self)