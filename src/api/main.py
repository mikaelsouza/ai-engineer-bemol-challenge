import client
from flask import Flask, jsonify

app = Flask(__name__)

data_path = 'data/processed/confidential_rfm.csv'
client_path = 'data/bin/CLIENTLABELS.BIN'
country_path = 'data/bin/COUNTRYIDS.BIN'

client_informer = client.ClientInformer(data_path=data_path,
                                        client_path=client_path,
                                        country_path=country_path)


def sane_input(id: str) -> int:

    try:
        id = int(id)
    except ValueError:
        print("Valor do tipo incorreto. Por favor insira um valor numérico.")
        id = None
    return id


@app.route('/')
def hello():
    return "Hello"


@app.route('/country/<id>')
def get_clients_by_country(id):
    id = sane_input(id)
    result = jsonify(client_informer.get_clients_by_country(id))
    return result


@app.route('/countries/')
def get_countries():
    result = jsonify(client_informer.get_countries())
    return result


@app.route('/client/<id>')
def get_client_by_id(id):
    id = sane_input(id)
    result = jsonify(client_informer.get_client_by_id(id))
    return result


@app.route('/tiers/')
def get_tiers():
    result = jsonify(client_informer.get_tiers())
    return result


@app.route('/tier/<id>')
def get_client_by_tier(id):
    id = sane_input(id)
    result = jsonify(client_informer.get_client_by_tier(id))
    return result
