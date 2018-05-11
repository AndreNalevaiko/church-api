import logging
from flask import Blueprint, request
from flask_cors import cross_origin
from datetime import datetime

from church_api import db
from church_api.model import Person
from church_api.config import API_VERSION

logger = logging.getLogger(__name__)

actions = Blueprint('abstract_products', __name__,
                    url_prefix='/abstract_products')

@actions.route('/_add_presence', methods=['POST'])
@cross_origin()
def _add_presence():
    data = request.get_json()

    person = Person.query.get(data['person_id'])

    if not person.last_presense_at or person.last_presense_at.day < datetime.utcnow().day:
        person.presences =+ 1
        person.last_presense_at = datetime.utcnow()

        db.session.add(person)
        db.session.commit()


def before_post(data=None, **kw):
    data['presences'] = 0
        

def create_api(api):
    api.create_api(Person,
                   methods=['GET', 'POST', 'PATCH'],
                   url_prefix='/%s' % API_VERSION,
                   results_per_page=10,
                   primary_key='id',
                   preprocessors={
                       'POST': [before_post]
                   },
                   postprocessors={
                   })