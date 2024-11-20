"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: Navpreet Kaur
Date: 27-09-2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        """Set up a BankAccount instance for testing."""
        self.account = BankAccount(2001, 1010, 1000.00)

    def test_initialization(self):
        """Test that the BankAccount initializes correctly with valid inputs."""
        self.assertEqual(self.account.account_number, 2001)
        self.assertEqual(self.account.client_number, 1010)
        self.assertEqual(self.account.balance, 1000.00)

    def test_invalid_account_number(self):
        """Test that initializing with a non-integer account_number raises ValueError."""
        with self.assertRaises(ValueError):
            BankAccount("not_an_int", 1010, 1000.00)

    def test_invalid_client_number(self):
        """Test that initializing with a non-integer client_number raises ValueError."""
        with self.assertRaises(ValueError):
            BankAccount(2002, "not_an_int", 1000.00)

    def test_invalid_balance(self):
        """Test that initializing with a non-float balance sets balance to 0.0."""
        account = BankAccount(2003, 1010, "invalid_balance")
        self.assertEqual(account.balance, 0.0)

    def test_deposit_valid(self):
        """Test depositing a valid positive amount."""
        self.account.deposit(500.00)
        self.assertEqual(round(self.account.balance, 2), 1500.00)

    def test_deposit_negative_amount(self):
        """Test depositing a negative amount raises ValueError."""
        with self.assertRaises(ValueError):
            self.account.deposit(-100.00)

    def test_deposit_non_numeric(self):
        """Test depositing a non-numeric amount raises ValueError."""
        with self.assertRaises(ValueError):
            self.account.deposit("not_a_number")

    def test_withdraw_valid(self):
        """Test withdrawing a valid amount."""
        self.account.withdraw(300.00)
        self.assertEqual(round(self.account.balance, 2), 700.00)

    def test_withdraw_exceeds_balance(self):
        """Test withdrawing an amount that exceeds the balance raises ValueError."""
        with self.assertRaises(ValueError):
            self.account.withdraw(1500.00)

    def test_withdraw_negative_amount(self):
        """Test withdrawing a negative amount raises ValueError."""
        with self.assertRaises(ValueError):
            self.account.withdraw(-200.00)

    def test_withdraw_non_numeric(self):
        """Test withdrawing a non-numeric amount raises ValueError."""
        with self.assertRaises(ValueError):
            self.account.withdraw("not_a_number")

    def test_update_balance_positive(self):
        """Test that update_balance correctly adds a positive amount."""
        self.account.update_balance(250.00)
        self.assertEqual(round(self.account.balance, 2), 1250.00)

    def test_update_balance_negative(self):
        """Test that update_balance correctly subtracts a negative amount."""
        self.account.update_balance(-150.00)
        self.assertEqual(round(self.account.balance, 2), 850.00)

    def test_update_balance_invalid(self):
        """Test that update_balance with invalid amount does not change balance."""
        original_balance = self.account.balance
        self.account.update_balance("invalid_amount")
        self.assertEqual(self.account.balance, original_balance)

    # Additional tests for service charges or observer pattern if applicable
    def test_service_charge_logic(self):
        """Test the service charge logic (if implemented)."""
        # You would need to set up the conditions for this test
        # For example, you could update the balance to trigger service charges
        pass

if __name__ == "__main__":
    unittest.main()
