from library.AbstractConnectionCreator import *
import sqlite3

# 정말 커넥션만 하는 코드!
class ConnectionCreator(AbstractConnectionCreator):
    def getConnection(self):
        return sqlite3.connect('test_strategy.db', isolation_level=None)