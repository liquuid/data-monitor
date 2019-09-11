from datetime import datetime
from flask import request
from app import app

@app.route('/')
def home():
 
    with open("db.csv", "a") as myfile:
        myfile.write("|".join([datetime.now().isoformat(), request.args.get('station', ''),request.args.get('temp', ''), request.args.get('humi', ''), '\n']))
    return "hello"
