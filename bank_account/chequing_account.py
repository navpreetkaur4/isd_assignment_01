"""
Description: This file defines the ChequingAccount class, which represents a chequing account with basic operations such as deposit and withdrawal.
Author:Navpreet 
Date: 06/10/2024
"""

from patterns.strategy.overdraft_strategy import OverdraftStrategy
from bank_account import BankAccount

class ChequingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit, overdraft_fee, service_charge):
        super().__init__(account_number, balance)
        # Initialize the strategy with appropriate arguments
        self._service_charge_strategy = OverdraftStrategy(
            overdraft_limit=overdraft_limit,
            overdraft_fee=overdraft_fee,
            service_charge=service_charge
        )
    
    def get_service_charges(self):
        # Call to calculate service charges using the strategy
        return self._service_charge_strategy.calculate_service_charges(self)
