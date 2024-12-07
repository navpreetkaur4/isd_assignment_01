from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSignal

class LookupWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Client Lookup')
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        self.lookup_button = QPushButton('Lookup Client', self)
        self.layout.addWidget(self.lookup_button)
        
        self.table_widget = QTableWidget(self)
        self.layout.addWidget(self.table_widget)
        
        self.lookup_button.clicked.connect(self.on_lookup_client)
        
    def reset_display(self):
        """Reset display (clear data, reset UI elements)"""
        self.table_widget.clear()
        
    def on_lookup_client(self):
        """Lookup client and display data"""
        print("Client lookup started.")
        # Logic to update the table with client data
        
class ClientLookupWindow(LookupWindow):
    def __init__(self):
        super().__init__()
        self.client_listing = {}  # Dictionary to store client data
        self.accounts = {}  # Dictionary to store account details
        
    def on_select_account(self, row, column):
        """Handle account selection"""
        account_number = self.table_widget.item(row, column).text()
        balance = self.accounts.get(account_number, {}).get('balance', 'N/A')
        print(f"Selected Account: {account_number} - Balance: {balance}")
    
    def update_data(self, account_number, balance):
        """Update account data"""
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] = balance
        print(f"Updated Account {account_number} with new balance: {balance}")
        
    def on_filter_clicked(self):
        """Handle filter clicked"""
        print("Filter clicked.")
        
    def toggle_filter(self, filter_on):
        """Toggle filter visibility"""
        if filter_on:
            print("Filter is ON.")
        else:
            print("Filter is OFF.")
