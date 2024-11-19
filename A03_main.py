"""
Description: A client program written to verify implementation 
of the Observer Pattern.
Author: ACE Faculty
Edited by: {Navpreet kaur}
Date: {Date}
"""

# Import necessary classes
from patterns.observer.subject import Subject
from patterns.observer.observer import Observer
from client.client import Client  # Adjust this import according to your structure
from bank_account import BankAccount  # Adjust this import according to your structure

def main():
    # Create instances of Client
    client1 = Client("Alice", "Smith", "12345")
    client2 = Client("Bob", "Johnson", "67890")

    # Create a BankAccount instance
    account1 = BankAccount("ACC001", 200.00)
    
    # Attach clients as observers
    account1.attach(client1)
    account1.attach(client2)

    # Perform a series of transactions
    transactions = [
        (150.00, "Deposit"),  # Regular deposit
        (-175.00, "Withdrawal"),  # Withdrawal that causes low balance
        (1200.00, "Deposit"),  # Large deposit transaction
        (-25.00, "Withdrawal")  # Small withdrawal
    ]

    for amount, transaction_type in transactions:
        try:
            print(f"{transaction_type} of ${amount:.2f} on account {account1.account_number}")
            account1.update_balance(amount)  # Update the account balance
        except Exception as e:
            print(f"An error occurred during the {transaction_type.lower()}: {e}")

if __name__ == "__main__":
    main()
