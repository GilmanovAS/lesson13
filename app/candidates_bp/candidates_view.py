from flask import Blueprint, render_template
from app.candidates_bp.dao_candidates.candidates_dao import CandidatesDAO
from configs.config import JSON_LOAD_PATH

candidates_blueprint = Blueprint('candidates_blueprint', __name__, template_folder='candidates_templates')


@candidates_blueprint.route('/candidates/')
def candidates_page():
    candidates = CandidatesDAO(JSON_LOAD_PATH)
    return render_template('candidates.html', candidates=candidates.get_all())

@candidates_blueprint.route('/candidates/<skill>')
def candidates_by_skill_page(skill):
    candidates = CandidatesDAO(JSON_LOAD_PATH)
    return render_template('candidates.html', candidates=candidates.get_by_skill(skill))
