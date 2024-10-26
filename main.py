from src.CSV.csv import CsvReader
from sklearn.ensemble import RandomForestClassifier


CSV_DIR = "./public/activitats.csv"

if __name__ == "__main__":
    csv_reader = CsvReader(CSV_DIR)

    data = csv_reader.data()

    clf = RandomForestClassifier(random_state=0)
    X = [[1, 2, 3],  # 2 samples, 3 features
         [11, 12, 13]]
    y = [0, 1]
    a = clf.fit(X, y)
    b = clf.predict(X)
    print(b)