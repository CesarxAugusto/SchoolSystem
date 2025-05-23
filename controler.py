import sqlite3

conn = sqlite3.connect('students.db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            gender TEXT NOT NULL,
            status BLOB,
            cpf TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL)
""")

conn.commit()
conn.close()