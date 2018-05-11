import logging
from flask import Blueprint, request, make_response
from flask_cors import cross_origin
from datetime import datetime

from church_api import db
from church_api.model import Person
from church_api.config import API_VERSION

logger = logging.getLogger(__name__)

actions = Blueprint('person', __name__,
                    url_prefix='/person')

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


@actions.route('/_return_photo/<int:id>', methods=['GET'])
@cross_origin()
def _return_photo(id):
    person = Person.query.get(id)
    photo = person.photo

    response = make_response(photo)
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='imagem.png')
    return response


def before_post(data=None, **kw):
    data['presences'] = 0

    if data.get('photo'):
        my_str_as_bytes = str.encode(data['photo'])
        type(my_str_as_bytes) # ensure it is byte representation
        my_decoded_str = my_str_as_bytes.decode()
        type(my_decoded_str)

        data['photo'] = my_str_as_bytes


def before_patch(instance_id=None, data=None, **kw):
    data['presences'] = 0

    if data.get('photo'):
        my_str_as_bytes = str.encode(data['photo'])
        type(my_str_as_bytes) # ensure it is byte representation
        my_decoded_str = my_str_as_bytes.decode()
        type(my_decoded_str)

        data['photo'] = my_str_as_bytes
        

def create_api(api):
    api.create_api(Person,
                   methods=['GET', 'POST', 'PATCH', 'DELETE'],
                   url_prefix='/%s' % API_VERSION,
                   results_per_page=10,
                   primary_key='id',
                   preprocessors={
                       'POST': [before_post],
                       'PATCH_SINGLE': [before_patch],
                   },
                   postprocessors={
                   })