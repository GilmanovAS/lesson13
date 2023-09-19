""" It's vacancies file"""
from flask import Blueprint, render_template

from app.vacancies_bp.dao_vacancies.vacancies_dao_f import VacanciesDAO
from configs.config import JSON_VACANCIES_PATH

vacancies_blueprint = Blueprint('vacancies_blueprint', __name__, template_folder='vacancies_templates')


@vacancies_blueprint.route('/vacancies/')
def vacancies_page():
    """It's vacation page"""
    print(vacancies_page.__doc__)
    vacancies_all = VacanciesDAO(JSON_VACANCIES_PATH)
    return render_template('vacancies.html', vacancies=vacancies_all.get_all())


@vacancies_blueprint.route('/vacancies/<position>')
def vacancies_by_position_page(position):
    vacancies_by_position = VacanciesDAO(JSON_VACANCIES_PATH)
    return render_template('vacancies.html', vacancies=vacancies_by_position.get_by_position(position))
