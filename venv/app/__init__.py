from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app import routes
app.config['DEBUG'] = True
app.config['MONGO_URI'] = 'mongodb+srv://root:root@cluster0.rbezrxz.mongodb.net/mcl?retryWrites=true&w=majority'
app.run()

