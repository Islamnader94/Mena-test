from flask import Flask
from marshmallow import Schema, fields, pre_load, validate, ValidationError
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Access(db.Model):
    __tablename__ = 'access'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone =  db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, name, address, email, phone):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone

class AccessSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    address  = fields.String(required=True)
    email = fields.String(required=True)
    phone =fields.String(required=True)