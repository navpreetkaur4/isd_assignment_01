"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Modified by: {navpreet kaur}
Date: {27-09-2024}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

import unittest
from client.client import Client

class TestClient(unittest.TestCase):
    def setUp(self):
        """Set up a Client instance for testing."""
        self.client = Client(1010, "Susan", "Clark", "susanclark@pixell.com")

    def test_initialization(self):
        """Test that the Client initializes correctly with valid inputs."""
        self.assertEqual(self.client.client_number, 1010)
        self.assertEqual(self.client.first_name, "Susan")
        self.assertEqual(self.client.last_name, "Clark")
        self.assertEqual(self.client.email_address, "susanclark@pixell.com")

    def test_invalid_client_number(self):
        """Test that initializing with a non-integer client_number raises ValueError."""
        with self.assertRaises(ValueError):
            Client("not_an_int", "John", "Doe", "john.doe@pixell.com")

    def test_blank_first_name(self):
        """Test that initializing with a blank first_name raises ValueError."""
        with self.assertRaises(ValueError):
            Client(1011, "   ", "Doe", "john.doe@pixell.com")

    def test_blank_last_name(self):
        """Test that initializing with a blank last_name raises ValueError."""
        with self.assertRaises(ValueError):
            Client(1012, "John", "   ", "john.doe@pixell.com")

    def test_invalid_email(self):
        """Test that initializing with an invalid email sets the default email."""
        client = Client(1013, "Jane", "Doe", "invalid-email")
        self.assertEqual(client.email_address, "email@pixell-river.com")

    def test_valid_email_with_whitespace(self):
        """Test that email is correctly stripped and validated."""
        client = Client(1014, "Jane", "Doe", "   jane.doe@pixell.com   ")
        self.assertEqual(client.email_address, "jane.doe@pixell.com")

if __name__ == "__main__":
    unittest.main()
