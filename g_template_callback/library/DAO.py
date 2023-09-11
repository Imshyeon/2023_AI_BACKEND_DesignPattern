from abc import *

class DAO():
    def __init__(self, fn): 
        self.getConnection = fn # 함수 주입 -> 메서드가 될 것임. => 파이썬이 함수를 1급 객체로 제공하기 때문에 사용이 가능한 것이다.
        
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