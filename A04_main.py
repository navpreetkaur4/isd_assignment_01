from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi

class ClientLookupWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('path_to_ui_file.ui', self)

        # Connect the filter button's clicked event to on_filter_clicked
        self.filter_button.clicked.connect(self.on_filter_clicked)

        # Initial toggle state: Filtering is not active
        self.toggle_filter(False)

    def on_filter_clicked(self):
        """
        Handles the filtering logic when the filter button is clicked.
        """
        if self.filter_button.text() == "Apply Filter":
            # Apply filtering
            filter_index = self.filter_combo_box.currentIndex()
            filter_value = self.filter_edit.text().lower()

            for row in range(self.account_table.rowCount()):
                item = self.account_table.item(row, filter_index)
                if filter_value in item.text().lower():
                    self.account_table.setRowHidden(row, False)  # Show matching rows
                else:
                    self.account_table.setRowHidden(row, True)  # Hide non-matching rows

            # Indicate filtering is active
            self.toggle_filter(True)

        else:
            # Reset filtering (show all rows)
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

            # Indicate filtering is not active
            self.toggle_filter(False)

    def toggle_filter(self, filter_on: bool):
        """
        Toggles the state of the filtering widgets and updates the filter label.
        :param filter_on: True if filtering is active, False otherwise.
        """
        if filter_on:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.clear()
            self.filter_combo_box.setCurrentIndex(0)
            self.filter_label.setText("Data is Not Currently Filtered")

    def on_lookup_client(self, client_number):
        """
        Fetches client data based on the client number and toggles filtering state.
        """
        # Fetch client data (mock example for demonstration)
        client_data_exists = self.fetch_client_data(client_number)  # Assume this method exists
        if client_data_exists:
            # Reset filtering widgets when client data is displayed
            self.toggle_filter(False)
        else:
            # Reset display (assume reset_display method exists)
            self.reset_display()

    def fetch_client_data(self, client_number):
        """
        Mock function to simulate fetching client data.
        Replace this with actual logic to fetch client data.
        """
        # Example: Returns True if the client exists, otherwise False
        return client_number in ["12345", "67890"]

    def reset_display(self):
        """
        Mock function to reset the display.
        Replace this with actual logic to reset the UI.
        """
        self.filter_button.setEnabled(False)
        self.filter_combo_box.setEnabled(False)
        self.filter_edit.setEnabled(False)
        self.filter_label.setText("No Client Data Available")
