"""
Description: Unit tests for the InvestmentAccount class.
Author: {navpreet kaur}
"""

import unittest
from datetime import date, timedelta
from investment_account import InvestmentAccount


class TestInvestmentAccount(unittest.TestCase):
    """Unit tests for the InvestmentAccount class."""

    def setUp(self):
        """Sets up test cases."""
        self.account = InvestmentAccount("234567", 1000, date(2020, 1, 1), 2.00)

    def test_service_charge_under_ten_years(self):
        """Tests service charge calculation for an account under 10 years old."""
        self
