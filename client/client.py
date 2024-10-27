"""
Description: This file defines the Client class used to represent a bank client.
Author: Sukhtab Singh Warya
Date: 10/09/2024
"""
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import datetime

class Client(Observer):
    """
    The Client class represents an observer that gets notified of changes 
    in the subject, specifically for bank account activities.
    """

    def __init__(self, client_number, first_name, last_name):
        """
        Initialize the Client with necessary attributes.

        Parameters:
        client_number (str): Unique identifier for the client.
        first_name (str): The first name of the client.
        last_name (str): The last name of the client.
        """
        self.client_number = client_number
        self.first_name = first_name
        self.last_name = last_name

    def update(self, message):
        """
        Update method that gets called when the subject notifies the observer.

        Parameters:
        message (str): The notification message from the subject.
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        subject_line = f"ALERT: Unusual Activity: {current_time}"
        notification_message = f"Notification for {self.client_number}: {self.first_name} {self.last_name}: {message}"

        # Simulate sending an email
        simulate_send_email(subject_line, notification_message)
