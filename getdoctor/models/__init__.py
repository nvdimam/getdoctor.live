import uuid

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()

class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String())
    department_id = db.Column(db.String, db.ForeignKey('department.id'))
    department = db.relationship("Department", backref=db.backref("service", uselist=False))


class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String())
    image = db.Column(db.String())
    short_desc = db.Column(db.String())
    desc = db.Column(db.String())
    category = db.Column(db.String())
    language = db.Column(db.String())
    service_id = db.Column(db.String, db.ForeignKey('service.id'))
    service = relationship("Service", backref=db.backref("department", uselist=False))
    
   


    # id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    # username = db.Column(db.String())
    # email = db.Column(db.String(), unique=True)