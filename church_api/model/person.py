
from sqlalchemy import event

from .base import ModelBase
from church_api import db
from church_api.helpers import input_audit_data_on_insert, input_audit_data_on_update


class Person(ModelBase, db.Model):
    first_name = db.Column(db.String(256), nullable=False)
    last_name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=True)
    photo = db.Column(db.LargeBinary(), nullable=False)
    church = db.Column(db.String(256), nullable=True)
    departure = db.Column(db.String(256), nullable=False)
    last_presense_at = db.Column(db.DateTime(), nullable=True)
    presences = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(256), nullable=True)
    

event.listen(Person, 'before_insert', input_audit_data_on_insert)
event.listen(Person, 'before_update', input_audit_data_on_update)