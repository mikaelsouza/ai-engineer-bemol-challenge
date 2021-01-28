import pandas as pd
import pickle
from pathlib import Path
from typing import Union


class ClientInformer(object):
    def __init__(self, data_path: Union[Path, str], country_path: Union[Path,
                                                                        str],
                 client_path: Union[Path, str]) -> None:
        super().__init__()
        # Setando caminhos
        self.data_path = data_path
        self.contry_path = country_path
        self.client_path = client_path

        # Carregando dados:
        self.data = pd.read_csv(self.data_path)
        with open(country_path, 'rb') as f:
            self.country_labels = pickle.load(f)
        with open(client_path, 'rb') as f:
            self.client_labels = pickle.load(f)

    def get_countries(self):
        '''
        Obtém o ID de todos os países existentes na base de dados.
        '''
        return self.country_labels

    def get_clients_by_country(self, country_id: int):
        '''
        Dado o ID de um país, retorna dados de todos os clientes do país especificado
        '''
        return self.data[self.data['Country'] == country_id].to_json(
            orient='records')

    def get_client_by_id(self, client_id: int):
        '''
        Dado o ID de um cliente, retorna dados daquele cliente
        '''
        return self.data[self.data['CustomerID'] == client_id].to_json(
            orient='records')

    def get_tiers(self):
        '''
        Obtém o ID de todos os tiers de clientes da base de dados
        '''
        return self.client_labels

    def get_client_by_tier(self, tier: int):
        '''
        Dado o tier de cliente, obtém todos os clientes contendo aquele tier
        '''
        return self.data[self.data['Label'] == tier].to_json(orient='records')
