import sqlite3

conn = sqlite3.connect('students.db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            gender TEXT NOT NULL,
            status TEXT NOT NULL,
            cpf TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            phone TEXT NOT NULL)
""")

conn.commit()
conn.close()

def insert_student(name, gender, status, cpf, email, phone):
    try:
        conn = sqlite3.connect('students.db')
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO students (name, gender, status, cpf, email, phone)
                    VALUES (?, ?, ?, ?, ?, ?)""", (name, gender, status, cpf, email, phone))
        conn.commit()
        conn.close()
        return True, "Estudante inserido com sucesso"
    except sqlite3.IntegrityError as e:
        return False, f"Erro de integridade: {str(e)}"

    except Exception as e:
        return False, f"Erro ao inserir usuário: {str(e)}"
    