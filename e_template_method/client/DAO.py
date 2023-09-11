from library.AbstractDAO import *
import sqlite3

class DAO(AbstractDAO): 
    def getConnection(self):    # 사용자가 getConnection 하도록 함.
        return sqlite3.connect('template_method.db', isolation_level=None) 
    
    
#template_method : 전체적인 기능 구현 메서드를 구현되어 있고, 빈칸이 있다. -> 그 빈칸을 채우면 전체 기능이 완성되는 디자인 패턴.