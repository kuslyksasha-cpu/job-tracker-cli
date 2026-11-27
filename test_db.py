import pytest
import db

@pytest.fixture(autouse=True)
def setup_test_db(tmp_path):
    db.DB_NAME = str(tmp_path / "test.db")
    db.init_db()

def test_add_and_get_vacancies():
    db.add_vacancy("Google", "Junior", "-")
    rows = db.get_all_vacancies()
    assert len(rows) == 1
    assert rows[0][1] == "Google"

def test_update_vacancy_status():
    db.add_vacancy("Google", "Junior", "-")
    rows = db.get_all_vacancies()
    vacancy_id = rows[0][0]
    updated = db.update_vacancy_status(1, "interview")
    assert updated == 1
    rows = db.get_all_vacancies()[0][4]
    assert rows == "interview"

def test_delete_vacancy():
    db.add_vacancy("Google", "Junior", "-")
    rows = db.get_all_vacancies()
    vacancy_id = rows[0][0]
    deleted = db.delete_vacancy(vacancy_id)
    assert deleted == 1
    rows = db.get_all_vacancies()
    assert len(rows) == 0

def test_search_and_filter():
    db.add_vacancy("Google", "Junior", "-")
    db.add_vacancy("Microsoft", "Senior", "-")
    search_results = db.search_by_company("Google")
    assert len(search_results) == 1
    assert search_results[0][1] == "Google"
    filter_results = db.filter_by_status("applied")
    assert len(filter_results) == 2