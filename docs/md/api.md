# API de Busca de Informação de Clientes

A API foi desenvolvida com o foco em utilizar chaves para buscar clientes na base de dados, além de permitir a descoberta das possíveis chaves de serem utilizadas.

Podemos dividir os endpoints em dois tipos.

1. Endpoints de Informação Geral: São utilizados para buscar o significado das possíveis chaves utilizadas.

2. Endpoints de Busca: São utilizadas para realizar buscas a partir de uma chave com o objetivo de retornar dados de clientes. Os dados de clientes são retornados como dicionários com os campos `CustomerID`, que representa o identificador do cliente, `Country` que representa o ID do país do cliente e `Label` que representa o tipo ou tier do cliente.

## 1. Endpoints de Informação Geral:

* `url/countries/`: Retorna um dicionário contendo todos os países existentes na base de dados e seus respectivos números identificadores.
* `url/tiers/`: Retorna um dicionário contendo todos os tiers de clientes e o que os valores representam.

## 2. Endpoints de Busca:

* `url/country/<id>`: Retorna uma lista de dicionários com informações de todos os clientes que pertencem àquele país.
* `url/tier/<id>`: Retorna uma lista de dicionários com informações de todos os clientes que pertencem àquele tier.
* `url/client/<id>`: Retorna uma lista de dicionários com a informação de um cliente específico.

## Informações de Tiers e Países:

Os seguintes dicionários correspondem aos valores de Tier e de ID de países armazenados na base de dados:

```python
# Tier
{
    "0": "Comum",
    "1": "Recorrente",
    "2": "Premium",
    "3": "Ex-Cliente"
}

# ID-Países
{
    "Australia": 0,
    "Austria": 1,
    "Bahrain": 2,
    "Belgium": 3,
    "Brazil": 4,
    "Canada": 5,
    "Channel Islands": 6,
    "Cyprus": 7,
    "Czech Republic": 8,
    "Denmark": 9,
    "EIRE": 10,
    "European Community": 11,
    "Finland": 12,
    "France": 13,
    "Germany": 14,
    "Greece": 15,
    "Iceland": 16,
    "Israel": 17,
    "Italy": 18,
    "Japan": 19,
    "Lebanon": 20,
    "Lithuania": 21,
    "Malta": 22,
    "Netherlands": 23,
    "Norway": 24,
    "Poland": 25,
    "Portugal": 26,
    "RSA": 27,
    "Saudi Arabia": 28,
    "Singapore": 29,
    "Spain": 30,
    "Sweden": 31,
    "Switzerland": 32,
    "USA": 33,
    "United Arab Emirates": 34,
    "United Kingdom": 35
}
```
