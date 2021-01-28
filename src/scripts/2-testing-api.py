import requests
import json
from os.path import join

# Modificar caso esteja usando outra porta ou acessando o serviço em núvem
url = 'http://127.0.0.1:5000/'

# Endpoints que não requerem IDs
countries_ep = 'countries'
tiers_ep = 'tiers'

# Endpoints que requerem IDs
country_ep = 'country'
client_ep = 'client'
tier_ep = 'tier'

# Exemplos:

# Requisitando ids de países:

req = join(url, countries_ep)

r = requests.get(req)
if r.status_code == requests.codes.ok:
    print("IDs de países: \n", json.loads(r.text))

# Requisitando ids de tiers:

req = join(url, tiers_ep)
r = requests.get(req)
if r.status_code == requests.codes.ok:
    print("IDs de tiers: \n", json.loads(r.text))

# Requisitando os clientes de um país - Brazil = 4

req = join(url, country_ep, '4')
r = requests.get(req)
if r.status_code == requests.codes.ok:
    print("Clientes do Brasil: \n", json.loads(r.text))

# Requisitando cliente pelo ID

req = join(url, client_ep, '12346')
r = requests.get(req)
if r.status_code == requests.codes.ok:
    print("Clientes por ID: \n", json.loads(r.text))

# Requisitando clientes por tier

req = join(url, tier_ep, '2')
r = requests.get(req)
if r.status_code == requests.codes.ok:
    print("Todos os clientes premium: \n", json.loads(r.text))
