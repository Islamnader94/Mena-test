from flask import request
from flask_restful import Resource
from Model import db, Access, AccessSchema
import json

all_access_schema = AccessSchema(many=True)
access_schema = AccessSchema()


class AccessResource(Resource):
    @staticmethod
    def get():
        all_access = Access.query.all()
        all_access = all_access_schema.dumps(all_access)
        return {'status': 'success', 'data': all_access}, 200
    @staticmethod
    def post():
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        response = json.dumps(json_data)
        data = access_schema.loads(response)
        access = Access.query.filter_by(name=data[0]['name']).first()
        if access:
            return {'message': 'User already exists'}, 400
        access = Access(
            name=data[0]['name'],
            address=data[0]['address'],
            email=data[0]['email'],
            phone=data[0]['phone']
            )

        db.session.add(access)
        db.session.commit()

        result = access_schema.dump(access)

        return {"status": 'success', 'data': result}, 201