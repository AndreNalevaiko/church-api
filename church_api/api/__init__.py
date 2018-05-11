import logging
from urllib.parse import urlparse
from flask import Flask
from flask_cors import CORS
from flask_restless.manager import APIManager
from church_api import config, db
from church_api.api import person
from church_api.helpers  import DefaultJSONEncoder

def create_blueprints(flask_app):
    flask_app.register_blueprint(person.actions)

def create_apis(api):
    person.create_api(api)

LOGGER = logging.getLogger(__name__)

app = Flask(__name__, static_folder="../static", template_folder="../templates")

app.config.from_object(config)

app.json_encoder = DefaultJSONEncoder

LOGGER.info('Configurado Flask')

CORS(app)

LOGGER.info("Configurado Ext Flask CORS")

db.init_app(app)

LOGGER.info('Configurado Extensão Flask SQLAlchemy')

api = APIManager(app=app, flask_sqlalchemy_db=db)

create_apis(api)

create_blueprints(app)





