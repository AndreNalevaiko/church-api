
from sqlalchemy import event

from .base import ModelBase
from church_api import db
from church_api.helpers import input_audit_data_on_insert, input_audit_data_on_update


class Person(ModelBase, db.Model):
    name = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(256), nullable=True)
    email = db.Column(db.String(256), nullable=True)
    photo = db.Column(db.LargeBinary(), nullable=False)
    active = db.Column(db.Boolean, nullable=True)
    occupation = db.Column(db.String(256), nullable=False)
    
    

event.listen(Person, 'before_insert', input_audit_data_on_insert)
event.listen(Person, 'before_update', input_audit_data_on_update)