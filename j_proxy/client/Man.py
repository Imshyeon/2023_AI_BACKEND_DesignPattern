from library.Developer import *
from library.ProxyDeveloper import *

class Man(Developer):
    
    def __new__(cls):
        return ProxyDeveloper(super().__new__(cls))
    
    def develop(self):
        print('javascript로 개발한다.')
        
            
    