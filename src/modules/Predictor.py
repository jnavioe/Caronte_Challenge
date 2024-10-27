from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


class Predictor:
    def __init__(self):
        self._model = None

    def train(self, students, x, y, test_size = 0.2):
        self._model = RandomForestRegressor(n_estimators=100, random_state=42)
        self._model.fit(x, y)

    def predict(self, x):
        return self._model.predict(x)[0]

