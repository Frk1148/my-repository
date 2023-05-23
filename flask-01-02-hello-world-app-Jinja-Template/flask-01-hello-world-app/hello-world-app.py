from flask import Flask

app = Flask(__name__)

def hello():
    return "<h1>Hello World</h1>"