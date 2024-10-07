"""
Description: Unit tests for the ChequingAccount class.
Author: {Your Name}
"""

import unittest
from datetime import date
from chequing_account import ChequingAccount


class TestChequingAccount(unittest.TestCase):
    """Unit tests for the ChequingAccount class."""

    def setUp(self):
        """Sets up test cases."""
        self.account = ChequingAccount("123456", 500, date(2022, 1, 1), -100, 0.05)

    def test_service_charge_within_limit(self):
        """Tests service charge calculation when balance is within the overdraft limit."""
        self.account.balance = -50  # Within overdraft limit
        self.assertEqual(round(self.account.get_service_charges(), 2), 0.50)

    def test_service_charge_below_limit(self):
        """Tests service charge calculation when balance is below the overdraft limit."""
        self.account.balance = -150  # Below overdraft limit
        self.assertEqual(round(self.account.get_service_charges(), 2), 25.50)

    def test_service_charge_at_limit(self):
        """Tests service charge calculation when balance is at the overdraft limit."""
        self.account.balance = -100  # At overdraft limit
        self.assertEqual(round(self.account.get_service_charges(), 2), 0.50)

    def test_overdraft_rate_validation(self):
        """Tests the validation of overdraft rate."""
        account = ChequingAccount("654321", 500, date(2022, 1, 1), "invalid", "invalid")
        self.assertEqual(account.overdraft_limit, -100)
        self.assertEqual(account.overdraft_rate, 0.05)


if __name__ == "__main__":
    unittest.main()
