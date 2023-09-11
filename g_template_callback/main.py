from library.DAO import *
import sqlite3

if __name__ == '__main__':
    dao = DAO(lambda : sqlite3.connect('template_callback.db', isolation_level=None))
    dao.create('CREATE TABLE users (id integer primary key, name text, age integer)')
    users = [
        ("hmd", 73),
        ("cyy", 12),
        ("hol", 48),
        ("htg", 87)
    ]        
    dao.insert('INSERT INTO users (name, age) VALUES (?, ?)', users)
    print(dao.select('SELECT * FROM users'))