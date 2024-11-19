"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""

# 1. Import all BankAccount types using the bank_account package
# Import date from datetime
from datetime import date
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing_acc = ChequingAccount(account_number="1234567", balance=-200.00, overdraft_limit=-100.00, overdraft_rate=0.05)

# 3. Print the ChequingAccount created in step 2.
print(chequing_acc)
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(f"Service Charges: ${chequing_acc.get_service_charges():.2f}\n")

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
chequing_acc.deposit(200.00)

# 4b. Print the ChequingAccount
print(chequing_acc)
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(f"Service Charges: ${chequing_acc.get_service_charges():.2f}\n")

print("===================================================")

# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
savings_acc = SavingsAccount(account_number="3456789", balance=1500.00, interest_rate=0.03)

# 6. Print the SavingsAccount created in step 5.
print(savings_acc)
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(f"Service Charges: ${savings_acc.get_service_charges():.2f}\n")

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
savings_acc.withdraw(1400.00)

# 7b. Print the SavingsAccount.
print(savings_acc)
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(f"Service Charges: ${savings_acc.get_service_charges():.2f}\n")

print("===================================================")

# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
investment_acc_recent = InvestmentAccount(account_number="4567890", balance=10000.00, date_created=date(2020, 5, 15), management_fee=1.00)

# 9a. Print the InvestmentAccount created in step 8.
print(investment_acc_recent)
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(f"Service Charges: ${investment_acc_recent.get_service_charges():.2f}\n")

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
investment_acc_old = InvestmentAccount(account_number="5678901", balance=5000.00, date_created=date(2008, 3, 22), management_fee=2.00)

# 11a. Print the InvestmentAccount created in step 10.
print(investment_acc_old)
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(f"Service Charges: ${investment_acc_old.get_service_charges():.2f}\n")

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8, and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.

chequing_acc.withdraw(chequing_acc.get_service_charges())
savings_acc.withdraw(savings_acc.get_service_charges())
investment_acc_recent.withdraw(investment_acc_recent.get_service_charges())
investment_acc_old.withdraw(investment_acc_old.get_service_charges())

# 13. Print each of the bank account objects created in steps 2, 5, 8, and 10.
print(chequing_acc)
print(savings_acc)
print(investment_acc_recent)
print(investment_acc_old)
