from flask_restful import Api, Resource
from flask import request
from app import app
from app.util import retrieve_data, upload_links, create_presigned_url

api = Api(app)

class Details(Resource):
    response = {"status": 400, "message": "Details not stored"}

    def post(self):
        user_data = request.get_json()
        retrieve_data(user_data)
        self.response["status"] = 201
        self.response["message"] = "Details stored successfully"

        return self.response, 201

api.add_resource(Details, "/details")

class GetUploadURL(Resource):
    response = {"status": 400, "message": "URL not generated"}

    def get(self):
        url = create_presigned_url()
        self.response["status"] = 201
        self.response["message"] = url

        return self.response, 201

api.add_resource(GetUploadURL, "/getuploadurl")


class UploadLinks(Resource):
    response = {"status": 400, "message": "Documents not uploaded"}

    def post(self):
        links = request.get_json()
        upload_links(links)
        self.response["status"] = 201
        self.response["message"] = "Document uploaded successfully!"

        return self.response, 201

api.add_resource(UploadLinks, "/uploaddetails")