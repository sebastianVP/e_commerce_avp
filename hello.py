'''
test de flask
'''
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Este TEST ES EL HOLA MUNDO, QUE TAL WENDY B, My first WEB APP- READY"
