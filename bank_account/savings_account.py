"""
Description: This module defines the SavingsAccount class, which extends the BankAccount class.
Author: Navpreet
Date: 06/10/2024
"""

from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, minimum_balance, penalty_fee):
        super().__init__(account_number, balance)
        # Initialize MinimumBalanceStrategy with minimum balance and penalty fee
        self._minimum_balance_strategy = MinimumBalanceStrategy(minimum_balance, penalty_fee)

    def get_service_charges(self):
        # Delegate service charge calculation to the MinimumBalanceStrategy
        return self._minimum_balance_strategy.calculate_service_charges(self)
