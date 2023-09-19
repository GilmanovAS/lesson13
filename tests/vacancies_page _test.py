import pytest
from main_app import app

class TestVacanciesPage:
    def test_vacancies_page(self, test_app):
        response = test_app.get('http://127.0.0.1:5000/vacancies/', follow_redirects=True)
        assert response.status_code == 200, "Error vacancies status code "
        assert 'dev' in response.data.decode('UTF-8').lower(), "Error on the vacancies page"
        pass