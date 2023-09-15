import logging
from flask import Flask
from app.main_bp.main_view import main_blueprint
from app.candidates_bp.candidates_view import candidates_blueprint

app = Flask(__name__)
app.config.from_pyfile('configs/config.py')

logging.basicConfig(level=app.config.get('LOG_LEVEL'), encoding='UTF-8')  # filename='log.log'
logging.info(app.config)

app.register_blueprint(main_blueprint)
app.register_blueprint(candidates_blueprint)

if __name__ == '__main__':
    app.run()
