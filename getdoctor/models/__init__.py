import uuid

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()


class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String())


class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String())
    image = db.Column(db.String())
    short_desc = db.Column(db.String())
    
    # image = db.Column(db.String())
    # short_desc = db.Column(db.String())
    # desc = db.Column(db.String())
    # service = service


    # id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    # username = db.Column(db.String())
    # email = db.Column(db.String(), unique=True)