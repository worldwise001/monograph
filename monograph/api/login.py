from typing import Dict, Any

from crossref.restful import Members
from flask import request
from flask_restful import Resource

from monograph.database.database import User


class LoginAPI(Resource):
    def post(self):
        body = request.get_json()
        user = body.get('username')
        password = body.get('password')

        authorized = (user == 'admin') and (password == 'admin')

        if not authorized:
            return {'error': 'Incorrect username or password'}, 401

        # Else
        return {'sucess': f'Welcome {user}'}
