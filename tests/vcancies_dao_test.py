import pytest
from app.vacancies_bp.dao_vacancies.vacancies_dao_f import VacanciesDAO
from main_app import app


@pytest.fixture()
def fix_vacanies_dao():
    return VacanciesDAO(app.config.get('JSON_VACANCIES_PATH'))


key_should_be = {"pk", "company", "position", "salary"}


class TestVacanciesDAO:
    def test_get_all(self, fix_vacanies_dao):
        vacancies = fix_vacanies_dao.get_all()
        assert set(vacancies[0].keys()) == key_should_be, "Incorrect list"
        assert type(vacancies) == list, "NOT list"
        assert len(vacancies) > 0, "Empty list"

    def test_by_skill(self, fix_vacanies_dao):
        vacancies = fix_vacanies_dao.get_by_position('Dev')
        assert vacancies[0]["pk"] == 2, "Inccorect number"
        assert key_should_be == set(vacancies[0].keys()), "Inccorect number"
