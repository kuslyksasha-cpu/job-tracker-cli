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
                status TEXT,
                url TEXT,
                created_at TEXT DEFAULT (DATE('now'))
            )
            """
        )

def search_by_company(query):
    with sqlite3.connect(DB_NAME) as conn:
        rows = conn.execute(
            "SELECT id, company, position, url, status, created_at FROM vacancies WHERE company LIKE ?",
            (f"%{query}%",)
        ).fetchall()
        return rows

def filter_by_status(status):
    with sqlite3.connect(DB_NAME) as conn:
        rows = conn.execute(
            "SELECT id, company, position, url, status, created_at FROM vacancies WHERE status = ?",
            (status,)
        ).fetchall()
        return rows

def get_stats():
    with sqlite3.connect(DB_NAME) as conn:
        rows = conn.execute(
            "SELECT status, COUNT(*) FROM vacancies GROUP BY status"
        ).fetchall()
        return rows

def add_vacancy(company, position, url):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            "INSERT INTO vacancies (company, position, url, status) VALUES (?, ?, ?, ?)",
            (company, position, url, "applied"),
        )

def get_all_vacancies():
    with sqlite3.connect(DB_NAME) as conn:
        rows = conn.execute(
            "SELECT id, company, position, url, status, created_at FROM vacancies"
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