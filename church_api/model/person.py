
from sqlalchemy import event

from .base import ModelBase
from church_api import db
from church_api.helpers import input_audit_data_on_insert, input_audit_data_on_update


class Person(ModelBase, db.Model):
    month = db.Column(db.Integer(), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    value = db.Column(db.DECIMAL(asdecimal=False, precision=17, scale=2), nullable=False)
    business_code = db.Column(db.Integer(), nullable=False)
    

event.listen(Person, 'before_insert', input_audit_data_on_insert)
event.listen(Person, 'before_update', input_audit_data_on_update)