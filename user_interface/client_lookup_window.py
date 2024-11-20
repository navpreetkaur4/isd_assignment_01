import copy
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QMessageBox, QVBoxLayout
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

# ClientLookupWindow.py
class ClientLookupWindow(LookupWindow):
    def __init__(self):
        super().__init__()
        self.client_listing, self.accounts = load_data()
        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.account_table.cellClicked.connect(self.on_select_account)

    def on_lookup_client(self):
        try:
            client_number = int(self.client_number_edit.text())
        except ValueError:
            QMessageBox.warning(self, "Non-Numeric Client", "Please enter a valid numeric client number.")
            self.reset_display()
            return
        
        if client_number not in self.client_listing:
            QMessageBox.warning(self, "Client Not Found", f"Client {client_number} not found.")
            self.reset_display()
            return
        
        client = self.client_listing[client_number]
        self.client_info_label.setText(f"Client: {client.first_name}")

        # print(f"Accounts available: {self.accounts}")
        # Add client accounts to accountTable
        self.account_table.setRowCount(0)  # Clear the table before adding new rows
        for account in self.accounts.values():
            if account.client_number == client_number:
                row_position = self.account_table.rowCount()
                self.account_table.insertRow(row_position)

                # Populate account details
                self.account_table.setItem(row_position, 0, QTableWidgetItem(str(account.account_number)))
                self.account_table.setItem(row_position, 1, QTableWidgetItem(f"${account.balance:,.2f}"))
                self.account_table.setItem(row_position, 2, QTableWidgetItem(account.date_created.strftime('%Y-%m-%d')))
                self.account_table.setItem(row_position, 3, QTableWidgetItem(account.__class__.__name__))
        
        # Resize columns to fit content
        self.account_table.resizeColumnsToContents()                

    def on_select_account(self, row, column):
        account_number = int(self.account_table.item(row, 0).text())
        print(f"Accounts available: {self.accounts}")
        if account_number in self.accounts:
            account = self.accounts[account_number]
            account_details_window = AccountDetailsWindow(account)
            account_details_window.balance_updated.connect(self.update_data)
            account_details_window.exec_()
        else:
            QMessageBox.warning(self, "Invalid Selection", "Please select a valid account.")

    def update_data(self, account: BankAccount):
        # Loop through the account_table to find the row that corresponds to the account number
        for row in range(self.account_table.rowCount()):
            account_number_item = self.account_table.item(row, 0)  # Assuming account number is in the first column
            if account_number_item and account_number_item.text() == str(account.account_number):
                self.account_table.item(row, 1).setText(f"{account.balance:.2f}")  # Update balance column
                self.accounts[account.account_number] = account  # Update accounts dictionary
                update_data(account)  # Call the manage_data module's update_data function
                break