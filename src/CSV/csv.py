import pandas as pd

class CsvReader:
    _data = None

    def __init__(self, dir):
        self._data = pd.read_csv(dir, encoding='utf-8', sep=',')
        print("hello")

    def data(self):
        return self._data.values
