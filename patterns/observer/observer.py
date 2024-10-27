class Observer:
    """
    The Observer superclass defines the interface for all concrete observers 
    that need to be notified of changes in the subject.
    """

    def update(self, message):
        """
        This method will be implemented in concrete observer classes 
        to handle notifications from the subject.
        
        Parameters:
        message (str): The notification message from the subject.
        """
        raise NotImplementedError("Subclass must implement abstract method.")
