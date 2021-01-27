import pandas as pd
from pathlib import Path
from typing import Union


class ClientInformer(object):
    def __init__(self, path: Union[Path, str]) -> None:
        super().__init__()
        self.path = path
        self.data = pd.read_csv(self.path)

        self.countries = self.data['Country'].unique()

    def get_countries(self):

