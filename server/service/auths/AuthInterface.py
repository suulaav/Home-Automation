from abc import ABC, abstractmethod


class AuthenticateInterface(ABC):
    @abstractmethod
    def authenticate(self, credential):
        pass
