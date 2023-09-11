import sqlite3

class DAO:
    def getConnection(self):    # 외부 환경에 따라서 변경해야 하는 코드.. 수정 해야하는 일이 잦다. 확장성이 좋지 않고 유연성이 떨어진다. -> client에게 위임하자!
        return sqlite3.connect('template_method.db', isolation_level=None)  # 경로는 일단 None으로 한 뒤, connection
    
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