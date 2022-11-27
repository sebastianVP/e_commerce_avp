'''
test de flask
'''
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "My first WEB APP- READY"