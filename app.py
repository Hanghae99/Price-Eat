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

SECRET_KEY = "SPARTA"

@app.route('/')
def home():
    return

@app.route('/login', methods=["POST"])
def login():
    id_receive = request.form['id']
    pw_receive = request.form['pw']
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    result = db.user.find_one({'id':id_receive,'pw':pw_hash}) # 매칭 되는 id와 pw 값이 있는지 확인
    if result is not None: # 데이터베이스에 result에 해당하는 id와 pw값이 있을경우
        payload = {
            'id' : id_receive,
            'exp' : datetime.utcnow() + datetime.itmedelta(minutes=3)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return

@app.route('/sign_up', mehtods=["POST"])
def sign_up():
    id_receive = request.form['id']
    pw_receive = request.form['pw']
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    name_receive = request.form['name']
    doc={
        'ID':id_receive,
        'password': pw_hash,
        'name':name_receive
    }
    db.user.insert_one(doc)
    return render_template('login.html')


