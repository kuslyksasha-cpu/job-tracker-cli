import sqlite3

DB_NAME = "vacancies.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS vacancies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company TEXT,
                position TEXT,
                status TEXT
            )
            """
        )

def add_vacancy(company, position):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            "INSERT INTO vacancies (company, position, status) VALUES (?, ?, ?)",
            (company, position, "sent"),
        )

def get_all_vacancies():
    with sqlite3.connect(DB_NAME) as conn:
        rows = conn.execute(
            "SELECT id, company, position, status FROM vacancies"
            ).fetchall()
        return rows

def update_vacancy_status(vacancy_id, new_status):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("UPDATE vacancies SET status = ? WHERE id = ?", (new_status, vacancy_id))
        return cursor.rowcount

def delete_vacancy(vacancy_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("DELETE FROM vacancies WHERE id = ?", (vacancy_id,))
        return cursor.rowcount