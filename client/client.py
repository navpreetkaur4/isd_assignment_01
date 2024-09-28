"""
Description: Client class for the banking system.
Author: [navpreet kaur]
"""

from email_validator import validate_email, EmailNotValidError

class Client:
    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        """
        Initializes a new Client instance with validated attributes.

        :param client_number: An integer representing the client number.
        :param first_name: The client's first name (non-blank).
        :param last_name: The client's last name (non-blank).
        :param email_address: The client's email address (valid format).
        :raises ValueError: If validations fail.
        """
        # Validate client_number
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        # Validate first_name
        stripped_first_name = first_name.strip()
        if not stripped_first_name:
            raise ValueError("First name cannot be blank.")
        self.__first_name = stripped_first_name

        # Validate last_name
        stripped_last_name = last_name.strip()
        if not stripped_last_name:
            raise ValueError("Last name cannot be blank.")
        self.__last_name = stripped_last_name

        # Validate email_address
        try:
            validated_email = validate_email(email_address)
            self.__email_address = validated_email.email
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"

    @property
    def client_number(self) -> int:
        """Gets the client number."""
        return self.__client_number

    @property
    def first_name(self) -> str:
        """Gets the first name."""
        return self.__first_name

    @property
    def last_name(self) -> str:
        """Gets the last name."""
        return self.__last_name

    @property
    def email_address(self) -> str:
        """Gets the email address."""
        return self.__email_address

    def __str__(self) -> str:
        """
        Returns formatted string representation of the Client.
        """
        return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}\n"
