from flask_restful import Api, Resource
from flask import request
from app import app
from app.util import *

api = Api(app)

class CreateUser(Resource):
    response = {"status": 400, "message": "User not created"}

    def post(self):
        user_data = request.get_json()
        retrieve_data(user_data)
        self.response["status"] = 201
        self.response["message"] = "User created successfully"

        return self.response, 201

api.add_resource(CreateUser, "/create")