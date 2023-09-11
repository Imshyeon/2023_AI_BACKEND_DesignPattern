from abc import *

class AbstractDAO(metaclass = ABCMeta): # 추상클래스
    
    @abstractmethod     # 추상클래스는 추상메소드가 구현되지 않으면 오류.  connection 객체를 반환하는 메서드를 만들자.
    def getConnection(self): pass
    
    def create(self, sql):
        try: 
            conn = self.getConnection()
            cursor = conn.cursor()
            cursor.execute(sql)
        finally:
            self. close(cursor, conn)
            
    def insert(self, sql, data):
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            cursor.executemany(sql, data)
            conn.commit()   # 문제가 없다면 커밋
        except:
            conn.rollback() # 문제가 생긴다면 롤백
        finally:
            self.close(cursor, conn)
            
    def select(self, sql):
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            cursor.execute(sql) # 쿼리 실행
            rows = cursor.fetchall()
            return rows
        finally:
            self.close(cursor, conn)
            
    def close(self, cursor, conn):
        cursor.close()
        conn.close()