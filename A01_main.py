""""
Description: A client program written to verify correctness of 
the BankAccount and Transaction classes.
Author: ACE Faculty
Edited by:Navpreet kaur
Date: {Date}
"""

from bank_account.bank_account import BankAccount
from client.client import Client
from email_validator import EmailNotValidError, validate_email

def main():
    # Testing Client class
    print("Testing Client Class:")
    try:
        client = Client(1010, "Susan", "Clark", "susanclark@pixell.com")
        print(f"Created Client: {client}")
    except ValueError as e:
        print(f"Error creating client: {e}")
    
    # Testing with an wrong email
    try:
        client_invalid = Client(1011, "John", "Doe", "invalid-email")
        print(f"Created Client: {client_invalid}")
    except EmailNotValidError as e:
        print(f"Email error: {e}")
    except ValueError as e:
        print(f"Error creating client: {e}")

    # Testing BankAccount class
    print("\nTesting BankAccount Class:")
    try:
        account = BankAccount(1001, 1010, 500.00)  # Valid account
        print(f"Created Bank Account: {account}")
        
        # Deposit
        account.deposit(100.00)
        print(f"Balance after deposit: {account.balance}")
        
        # Withdraw
        account.withdraw(50.00)
        print(f"Balance after withdrawal: {account.balance}")
        
        # Withdraw exceeding balance
        account.withdraw(1000.00)
    except ValueError as e:
        print(f"Transaction error: {e}")

if __name__ == "__main__":
    main()
