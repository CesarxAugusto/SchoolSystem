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

def delete_student_by_cpf(cpf):
    try:
        conn = sqlite3.connect('students.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM students WHERE cpf = ?", (cpf,))
        student = cur.fetchone()

        if not student:
            return False, "Nenhum aluno encontrado com esse CPF."

        cur.execute("DELETE FROM students WHERE cpf = ?", (cpf,))
        conn.commit()
        conn.close()
        return True, "Aluno deletado com sucesso."

    except sqlite3.IntegrityError as e:
        return False, f"Erro de integridade no banco de dados: {str(e)}"

    except sqlite3.Error as e:
        return False, f"Erro ao deletar aluno: {str(e)}"

def update_student_by_cpf(cpf, name=None, gender=None, status=None, phone=None, email=None):
    try:
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students WHERE cpf = ?", (cpf,))
        if cursor.fetchone() is None:
            conn.close()
            return False, "Nenhum aluno encontrado com esse CPF."

        fields = []
        values = []

        if name:
            fields.append("name = ?")
            values.append(name)
        if gender:
            fields.append("gender = ?")
            values.append(gender)
        if status:
            fields.append("status = ?")
            values.append(status)
        if phone:
            fields.append("phone = ?")
            values.append(phone)
        if email:
            fields.append("email = ?")
            values.append(email)

        if not fields:
            conn.close()
            return False, "Nenhuma informação fornecida para atualização."

        values.append(cpf)
        sql = f"UPDATE students SET {', '.join(fields)} WHERE cpf = ?"
        cursor.execute(sql, values)

        conn.commit()
        conn.close()
        return True, "Dados do aluno atualizados com sucesso."

    except sqlite3.Error as e:
        return False, f"Erro ao atualizar aluno: {str(e)}"