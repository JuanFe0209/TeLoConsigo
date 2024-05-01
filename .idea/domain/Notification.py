from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send_message(self, user):
        pass
