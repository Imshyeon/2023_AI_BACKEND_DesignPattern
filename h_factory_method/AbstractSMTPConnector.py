from abc import *

class AbstractSMTPConnector(metaclass = ABCMeta):
    @abstractmethod
    def connect(self):
        pass