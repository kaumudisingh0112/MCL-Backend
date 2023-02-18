from flask import Flask
from flask_pymongo import pymongo, PyMongo
from app import app

def get_bidder_data():
    mongodb_client = PyMongo(app)
    db = mongodb_client.db
    bidder_data = db.bidder_data
    return bidder_data

def get_document_links():
    mongodb_client = PyMongo(app)
    db = mongodb_client.db
    document_links = db.document_links
    return document_links