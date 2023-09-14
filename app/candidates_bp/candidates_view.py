from flask import Blueprint, render_template

candidates_blueprint = Blueprint('candidates_blueprint', __name__, template_folder='candidates_templates')

@candidates_blueprint.route('/candidates/')
def main_page():
    return render_template('candidates.html')
