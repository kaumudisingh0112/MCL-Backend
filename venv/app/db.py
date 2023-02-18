from flask import Flask
from flask_pymongo import pymongo, PyMongo
from app import app

def get_collection():
    mongodb_client = PyMongo(app)
    db = mongodb_client.db
    bidder_data = db.bidder_data
    return bidder_data