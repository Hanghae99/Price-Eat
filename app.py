import jwt
import datetime
import hashlib
from flask import *
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import dbconfig

app = Flask(__name__)
client = MongoClient(dbconfig.MONGODB_SETTING.values())
db = client.test

SWCRET_KEY = ""

@app.route('/')
def home():
    return

@app.route('/login', methods=["POST"])
def login():
    id = request.form['id']
    password = request.form['pw']

    return

@app.route('/sign_up', mehtods=["POST"])
def sign_up():
    id = request.form['id']
    password = request.form['pw']
    pw_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    name = request.form['name']
    doc={
        'ID':id,
        'password': pw_hash,
        'name':name
    }
    db.register.insert_one(doc)
    return render_template('login.html')


