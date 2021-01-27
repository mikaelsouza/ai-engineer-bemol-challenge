from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello"


@app.route('/country/<id>')
def get_clients_by_country(id):
    return {'data': "oi rs"}
