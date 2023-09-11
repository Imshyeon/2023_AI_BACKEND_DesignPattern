from abc import *

class DAO():
    def __init__(self, conn):
        self.conn = conn
        
    def create(self, sql):
        try: 
            conn = self.conn.getConnection()
            cursor = conn.cursor()
            cursor.execute(sql)
        finally:
            self. close(cursor, conn)
            
    def insert(self, sql, data):
        try:
            conn = self.conn.getConnection()
            cursor = conn.cursor()
            cursor.executemany(sql, data)
            conn.commit()   # 문제가 없다면 커밋
        except:
            conn.rollback() # 문제가 생긴다면 롤백
        finally:
            self.close(cursor, conn)
            
    def select(self, sql):
        try:
            conn = self.conn.getConnection()
            cursor = conn.cursor()
            cursor.execute(sql) # 쿼리 실행
            rows = cursor.fetchall()
            return rows
        finally:
            self.close(cursor, conn)
            
    def close(self, cursor, conn):
        cursor.close()
        conn.close()