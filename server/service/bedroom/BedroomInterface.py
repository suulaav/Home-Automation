from abc import ABC, abstractmethod


class BedroomInterface(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_data(self, user, request):
        pass
