"""
Description: Unit tests for the SavingsAccount class.
Author: {Your Name}
"""

import unittest
from datetime import date
from savings_account import SavingsAccount


class TestSavingsAccount(unittest.TestCase):
    """Unit tests for the SavingsAccount class."""

    def setUp(self):
        """Sets up test cases."""
        self.account = SavingsAccount("345678", 1000, date(2021, 1, 1))

    def test_service_charge(self):
        """Tests service charge calculation for the Savings Account."""
        self.assertEqual(round(self.account.get_service_charges(), 2), 0.50)  # Assuming flat service charge

    def test_account_string(self):
        """Tests the string representation of the Savings Account."""
        expected_string = "Account Number: 345678 Balance: $1000.00 Account Type: Savings"
        self.assertEqual(str(self.account), expected_string)


if __name__ == "__main__":
    unittest.main()
