from abc import *

class Developer(metaclass = ABCMeta): # 추상클래스에 의해서 Child, Woman, Man에 develop 메소드가 있음을 보장
    
    @abstractmethod
    def develop(self):
        pass 