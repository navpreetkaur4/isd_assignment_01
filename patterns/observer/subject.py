class Subject:
    """
    The Subject class is responsible for maintaining a list of its observers 
    and notifying them of state changes or events.
    """

    def __init__(self):
        """
        Initialize the Subject with an empty list of observers.
        """
        self._observers = []  # Protected attribute to hold observers

    def attach(self, observer):
        """
        Attach a new observer to the subject's list of observers.

        Parameters:
        observer (Observer): An observer object that wants to be notified of changes.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """
        Remove an observer from the subject's list of observers.

        Parameters:
        observer (Observer): The observer object to be removed.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message):
        """
        Notify all registered observers of a state change.

        Parameters:
        message (str): The message to send to all observers.
        """
        for observer in self._observers:
            observer.update(message)
