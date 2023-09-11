from abc import *

class AbstractConnectionCreator(metaclass=ABCMeta):
    @abstractmethod
    def getConnection(self):
        pass
