# Job Tracker CLI

Command-line application for tracking job and internship applications built with Python and SQLite.

## Tech Stack
- Python 3
- SQLite (`sqlite3`)
- `pytest` (unit testing)

## Features
- Add job applications (company, position, optional URL, automatic date)
- View all saved applications
- Update application status from a predefined list (`applied`, `test task`, `interview`, `offer`, `rejected`)
- Delete applications by ID
- Search applications by company name
- Filter applications by status
- View application statistics (total count and breakdown by status)

## Project Structure
- `main.py` — CLI menu, user input validation, and display logic
- `db.py` — SQLite database initialization and CRUD/query operations
- `test_db.py` — unit tests for database functions

## How to Run
```bash
python3 main.py
```

## Example Usage
```text
====================
1. add
2. show
3. change status
4. delete
5. search by company
6. filter by status
7. statistics
0. exit
====================

1. Google - Python Junior [https://careers.google.com](https://careers.google.com) [interview] 2026-11-27
2. Allegro - Backend Intern - [applied] 2026-11-27
```

## Running Tests
```bash
pip install pytest
pytest
```