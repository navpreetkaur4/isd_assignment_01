"""
Description: Unit tests for the InvestmentAccount class.
Author: Navpreet kaur
Date: 06/10/2024
"""


import unittest
from bank_account.investment_account import InvestmentAccount
from datetime import date, timedelta

class TestInvestmentAccount(unittest.TestCase):

    def setUp(self):
        """Set up a basic InvestmentAccount instance for testing."""
        self.account_valid = InvestmentAccount(59002635, 5550, 1200.00, date.today(), 2.00)

    def test_init_attributes(self):
        """Test __init__ to ensure attributes are set to parameter values."""
        self.assertEqual(self.account_valid.account_number, 59002635)
        self.assertEqual(self.account_valid.client_number, 5550)
        self.assertEqual(round(self.account_valid.balance, 2), 1200.00)
        self.assertEqual(self.account_valid.date_created, date.today())
        self.assertEqual(round(self.account_valid.management_fee, 2), 2.00)  # Changed to public attribute

    def test_init_invalid_management_fee_type(self):
        """Test __init__ when management fee has an invalid type."""
        account_invalid_fee = InvestmentAccount(59002635, 5550, 1200.00, date.today(), "invalid")
        self.assertEqual(round(account_invalid_fee.management_fee, 2), 2.55)  # Changed to public attribute

    def test_get_service_charges_date_created_more_than_10_years_ago(self):
        """Test get_service_charges when date created is more than 10 years ago."""
        account_old = InvestmentAccount(59002635, 5550, 1200.00, date.today() - timedelta(days=10*365.25))
        expected_charge = InvestmentAccount.BASE_SERVICE_CHARGE  # Assuming BASE_SERVICE_CHARGE is defined in your class
        self.assertEqual(round(account_old.get_service_charges(), 2), round(expected_charge, 2))

    def test_get_service_charges_date_created_exactly_10_years_ago(self):
        """Test get_service_charges when date created is exactly 10 years ago."""
        account_exact = InvestmentAccount(59002635, 5550, 1200.00, date.today() - timedelta(days=10*365.25))
        expected_charge = InvestmentAccount.BASE_SERVICE_CHARGE  # No additional fee
        self.assertEqual(round(account_exact.get_service_charges(), 2), round(expected_charge, 2))

    def test_get_service_charges_date_created_within_last_10_years(self):
        """Test get_service_charges when date created is within the last 10 years."""
        account_recent = InvestmentAccount(59002635, 5550, 1200.00, date.today(), 2.00)
        expected_charge = InvestmentAccount.BASE_SERVICE_CHARGE + 2.00  # Assuming BASE_SERVICE_CHARGE is defined
        self.assertEqual(round(account_recent.get_service_charges(), 2), round(expected_charge, 2))

    def test_str_displays_waived_management_fee_more_than_10_years_ago(self):
        """Test __str__ displays waived management fee when date created is more than 10 years ago."""
        account_old = InvestmentAccount(59002635, 5550, 1200.00, date.today() - timedelta(days=10*365.26))
        expected_str = ("Account Number: 59002635 Balance: $1200.00\n"
                        f"Date Created: {account_old.date_created} Management Fee: Waived Account Type: Investment")
        self.assertEqual(str(account_old), expected_str)

    def test_str_displays_management_fee_within_last_10_years(self):
        """Test __str__ displays management fee when date created is within last 10 years."""
        account_recent = InvestmentAccount(59002635, 5550, 1200.00, date.today(), 2.00)
        expected_str = ("Account Number: 59002635 Balance: $1200.00\n"
                        f"Date Created: {account_recent.date_created} Management Fee: $2.00 Account Type: Investment")
        self.assertEqual(str(account_recent), expected_str)

if __name__ == '__main__':
    unittest.main()
