import pandas as pd 
import numpy as np

class CsvReader:
    _data = None
    _splitData = None

    def __init__(self, dir):
        self._data = pd.read_csv(dir, encoding='utf-8', sep=',')
        self._splitData = np.array_split(self._data ,np.size(self._data, 0)/2, 0)
        
        print("hello")

    def data(self):
        return self._data.values
