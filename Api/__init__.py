import os

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql11497334:u1lUdt4f7n@sql11.freemysqlhosting.net:3306/sql11497334'

from Api import models
from Api import views
