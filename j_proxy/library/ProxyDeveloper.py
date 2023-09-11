# 공통적으로 작동하는 기능들 (출근 - 쉬는날 - 집)은 Proxy에서 전담하도록...
from library.Developer import *

class ProxyDeveloper(Developer):
    def __init__(self, dev):
        self.dev = dev
        
    def develop(self):  # 공통 로직
        print('출근 카드를 찍는다.')
        
        try:
            self.dev.develop()  # 공통 로직이 아닌 부분은 프록시의 타겟 객체에게 위임
        except:
            print('쉬는 날')
        finally:
            print('집')