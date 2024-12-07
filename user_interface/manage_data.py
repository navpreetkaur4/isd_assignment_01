import os
import sys
# THIS LINE IS NEEDED SO THAT THE GIVEN TESTING 
# CODE CAN RUN FROM THIS DIRECTORY.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import csv
from datetime import datetime
from bank_account.bank_account import BankAccount
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount
from client.client import Client
import logging

# *******************************************************************************
# GIVEN LOGGING AND FILE ACCESS CODE
 
# Absolute path to root of directory
root_dir = os.path.dirname(os.path.dirname(__file__))
 
# Path to the log directory relative to the root directory
log_dir = os.path.join(root_dir, 'logs')
 
# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok = True)
 
# Specify the path to the log file within the log directory
log_file_path = os.path.join(log_dir, 'manage_data.log')
 
# Configure logging to use the specified log file
logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s\n\n')
 
# Given File Path Code:
# Designed to locate the input files without providing any directory structure

# Construct the absolute path to the data directory at the root of the project
data_dir = os.path.join(root_dir, 'data')
 
# Construct the absolute paths to the data files
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')
 
# END GIVEN LOGGING AND FILE ACCESS CODE
# *******************************************************************************


def load_data()->tuple[dict,dict]:
    """
    Populates a client dictionary and an account dictionary with 
    corresponding data from files within the data directory.
    Returns:
        tuple containing client dictionary and account dictionary.
    """
    client_listing = {}
    accounts = {}

    # READ CLIENT DATA 
    try:
        # READ CLIENT DATA
        with open(clients_csv_path, newline='') as client_file:
            reader = csv.DictReader(client_file)
            for row in reader:
                try:
                    # Extract client information from each row
                    client_number = int(row['client_number'])  # Convert client_number to an integer
                    first_name = row['first_name'].strip()  # Strip any leading/trailing whitespace
                    last_name = row['last_name'].strip()    # Strip any leading/trailing whitespace
                    email = row['email_address'].strip()    # Strip any leading/trailing whitespace

                    # Check for mandatory fields, raise an exception if empty
                    if not first_name:
                        raise ValueError("First Name cannot be blank.")
                    if not last_name:
                        raise ValueError("Last Name cannot be blank.")
                    if not email:
                        raise ValueError("Email cannot be blank.")

                    # Construct a Client object (ensure the data types meet the Client class specifications)
                    client = Client(client_number, first_name, last_name, email)

                    # Add the Client object to the client_listing dictionary using client_number as the key
                    client_listing[client_number] = client

                except ValueError as ve:
                    logging.error(f"Unable to create client: {ve} - Client Data: {row}")
                except KeyError as ke:
                    logging.error(f"Missing expected column in client data: {ke} - Client Data: {row}")
                except Exception as e:
                    logging.error(f"Unexpected error while processing client data: {e} - Client Data: {row}")

        logging.info(f"Loaded {len(client_listing)} clients.")

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        

    # READ ACCOUNT DATA
    try:
        with open(accounts_csv_path, newline='') as account_file:
            reader = csv.DictReader(account_file)
            for row in reader:
                try:
                    # Extract account information from each row
                    account_number = int(row['account_number'])
                    client_number = int(row['client_number'])
                    balance = float(row['balance'])
                    date_created = datetime.strptime(row['date_created'], "%Y-%m-%d").date()
                    account_type = row['account_type']  # Account type (e.g., 'ChequingAccount', 'SavingsAccount', etc.)
                    overdraft_limit = float(row['overdraft_limit'])  # Overdraft limit as a float
                    base_service_charge = float(row['minimum_balance'])  # Base service charge
                    service_charge_premium = float(row['management_fee']) 

                    # Determine the account type and instantiate the correct subclass
                    if account_type == 'ChequingAccount':
                        account = ChequingAccount(account_number, 
                          client_number, 
                          balance, 
                          base_service_charge,
                          service_charge_premium,
                          overdraft_limit)
                    elif account_type == 'SavingsAccount':
                        account = SavingsAccount(account_number, 
                          client_number, 
                          balance, 
                          base_service_charge,
                          service_charge_premium)
                    elif account_type == 'InvestmentAccount':
                        account = InvestmentAccount(account_number, client_number, balance, date_created, service_charge_premium)
                    else:
                        logging.warning(f"Unknown account type '{account_type}' - Account Data: {row}")
                        continue  # Skip this row if the account type is not recognized

                    # Add the account data to the accounts dictionary
                    accounts[account_number] = account

                except ValueError as ve:
                    logging.error(f"Error parsing account data: {ve} - Account Data: {row}")
                except KeyError as ke:
                    logging.error(f"Missing expected column in account data: {ke} - Account Data: {row}")
                except Exception as e:
                    logging.error(f"Unexpected error while processing account data: {e} - Account Data: {row}")

        logging.info(f"Loaded {len(accounts)} accounts.")
    
    except FileNotFoundError as e:
        logging.error(f"Account file not found: {e}")
    except Exception as e:
        logging.error(f"Unexpected error while reading account file: {e}")

    # Return the populated dictionaries
    return client_listing, accounts
    


def update_data(updated_account: BankAccount) -> None:
    """
    A function to update the accounts.csv file with balance 
    data provided in the BankAccount argument.
    Args:
        updated_account (BankAccount): A bank account containing an updated balance.
    """
    updated_rows = []

    with open(accounts_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames
        
        for row in reader:
            account_number = int(row['account_number'])
            # Check if the account number is in the dictionary
            if account_number == updated_account.account_number:
                # Update the balance column with the new balance from the dictionary
                row['balance'] = updated_account.balance
            updated_rows.append(row)

    # Write the updated data back to the CSV
    with open(accounts_csv_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_rows)


# GIVEN TESTING SECTION:
if __name__ == "__main__":
    clients,accounts = load_data()

    print("=========================================")
    for client in clients.values():
        print(client)
        print(f"{client.client_number} Accounts\n=============")
        for account in accounts.values():
            if account.client_number == client.client_number:
                print(f"{account}\n")
        print("=========================================")