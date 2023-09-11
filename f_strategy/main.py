from library.DAO import *
from client.ConnectionCreator import *  # 커넥션 정보만 반환

if __name__ == '__main__':
    dao = DAO(ConnectionCreator())
    dao.create('CREATE TABLE users (id integer primary key, name text, age integer)')
    users = [
        ("hmd", 73),
        ("cyy", 12),
        ("hol", 48),
        ("htg", 87)
    ]        
    dao.insert('INSERT INTO users (name, age) VALUES (?, ?)', users)
    print(dao.select('SELECT * FROM users'))