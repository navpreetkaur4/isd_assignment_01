from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QMessageBox, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(QDialog):
    balance_updated = Signal(BankAccount)

    def __init__(self, account=None):
        super().__init__()

        # Step 1: Ensure the account parameter is a valid BankAccount instance
        if not isinstance(account, BankAccount):
            self.reject()  # Close the dialog if invalid
            return

        # Step 2: Copy the received account to the instance's attribute
        self.account = copy.copy(account)

        # Set window title and initial size
        self.setWindowTitle("Account Details")
        self.resize(150, 100)

        # Step 3: Initialize labels and buttons
        self.account_number_label = QLabel(f"Account Number: {self.account.account_number}")
        self.balance_label = QLabel(f"Balance: ${self.account.balance:,.2f}")

        # Transaction amount input and buttons
        self.transaction_amount_edit = QLineEdit()
        self.transaction_amount_edit.setPlaceholderText("Enter Amount")

        self.deposit_button = QPushButton("Deposit")
        self.withdraw_button = QPushButton("Withdraw")
        self.exit_button = QPushButton("Exit")

        # Step 4: Connect buttons to their handlers
        self.deposit_button.clicked.connect(self.on_apply_transaction)
        self.withdraw_button.clicked.connect(self.on_apply_transaction)
        self.exit_button.clicked.connect(self.on_exit)

        # Step 5: Layout management
        info_layout = QVBoxLayout()
        info_layout.addWidget(self.account_number_label)
        info_layout.addWidget(self.balance_label)
        info_layout.addWidget(self.transaction_amount_edit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.deposit_button)
        button_layout.addWidget(self.withdraw_button)
        button_layout.addWidget(self.exit_button)

        # Combine all layouts
        main_layout = QVBoxLayout()
        main_layout.addLayout(info_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def on_apply_transaction(self):
        """
        Handles deposit and withdrawal transactions.
        """
        try:
            # Step 1: Convert the input amount to a float
            amount = float(self.transaction_amount_edit.text())

            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")

            # Step 2: Determine which button was clicked (Deposit or Withdraw)
            sender = self.sender()
            transaction_type = ""

            if sender == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)  # Call deposit method of BankAccount
            elif sender == self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)  # Call withdraw method of BankAccount

            # Step 3: Update the balance label after transaction
            self.balance_label.setText(f"Balance: ${self.account.balance:,.2f}")
            self.transaction_amount_edit.clear()  # Clear the amount field
            self.transaction_amount_edit.setFocus()  # Set focus to the amount field

            # Emit signal after transaction
            self.balance_updated.emit(self.account)

        except ValueError as e:
            # Invalid input, display error message
            QMessageBox.warning(self, "Transaction Failed", f"Invalid amount entered: {str(e)}")
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()

        except Exception as e:
            # Handle other errors such as insufficient balance, etc.
            QMessageBox.warning(self, "Transaction Failed", f"Failed to process the transaction: {str(e)}")
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()

    def on_exit(self):
        """
        Confirms exit action and closes the dialog window.
        """
        reply = QMessageBox.question(
            self, "Confirm Exit", "Are you sure you want to exit?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.close()
