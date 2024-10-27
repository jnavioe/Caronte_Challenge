from src.entity.submission import Submission
from src.entity.activity import Activity
from src.entity.exam import Exam
from src.enum.exam import ExamType
from src.entity.student import Student
from src.CSV.csv import CsvReader
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

 
def prueba():
     students = []
    # Cargar los archivos CSV
     trameses = pd.read_csv('./public/trameses.csv',na_values = 0)
     activitats = pd.read_csv('./public/activitats.csv')
     examens = pd.read_csv('./public/notes.csv', delimiter=';', na_values = 0)
     

     #activitats prova
     '''
     activitats = activitats.fillna(0)
     #examens['P_Grade'] = pd.to_numeric(examens['P_Grade'], errors='coerce')
     #examens['F_Grade'] = pd.to_numeric(examens['F_Grade'], errors='coerce')
     #examens['R_Grade'] = pd.to_numeric(examens['R_Grade'], errors='coerce')
     #examens['P_Grade'] = examens['P_Grade'].astype(float)
     #examens['F_Grade'] = examens['F_Grade'].astype(float)
     #examens['R_Grade'] = examens['R_Grade'].astype(float)
     x = activitats['aula_id'].values.reshape(-1, 1)
     y = activitats['activitat_id'].values.reshape(-1, 1)

     X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=0)
     regressor = LinearRegression()
     regressor.fit(X_train, Y_train)
     y_pred = regressor.predict(X_train)
     print('Coefficients: \n', regressor.coef_)
     print('Independent term: \n', regressor.intercept_)
     print("Mean squared error: %.2f" % mean_squared_error(Y_train, y_pred))
     print('Variance score: %.2f' % r2_score(Y_train, y_pred))
     plt.scatter(X_train, Y_train, color='blue', label='Datos')
     plt.plot(X_train, y_pred, color='red', label='Recta de regresión')
     plt.xlabel('X')
     plt.ylabel('Y')
     plt.title('Regresión Lineal')
     plt.legend()

# Mostrar gráfico
     plt.show()
     # Obtener todos los 'userid' únicos
     sns.set(style='whitegrid', context='notebook')
     cols = ["aula_id","activitat_id"]
     print("jelou")
     activitats.hist()
     plt.show()
     sns.pairplot(activitats[cols], height=1.75);
     print("jelou2")
     '''

     #examens prova
    
     examens = examens.dropna(subset=['F_Grade'])
     examens = examens.dropna(subset=['R_Grade'])
     examens = examens.dropna(subset=['P_Grade'])
     examens = examens.fillna(0)
     #examens['P_Grade'] = pd.to_numeric(examens['P_Grade'], errors='coerce')
     #examens['F_Grade'] = pd.to_numeric(examens['F_Grade'], errors='coerce')
     #examens['R_Grade'] = pd.to_numeric(examens['R_Grade'], errors='coerce')
     #examens['P_Grade'] = examens['P_Grade'].astype(float)
     #examens['F_Grade'] = examens['F_Grade'].astype(float)
     #examens['R_Grade'] = examens['R_Grade'].astype(float)
     x = examens['F_Grade'].values.reshape(-1, 1)
     y = examens['R_Grade'].values.reshape(-1, 1)

     X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=0)
     regressor = LinearRegression()
     regressor.fit(X_train, Y_train)
     y_pred = regressor.predict(X_train)
     print('Coefficients: \n', regressor.coef_)
     print('Independent term: \n', regressor.intercept_)
     print("Mean squared error: %.2f" % mean_squared_error(Y_train, y_pred))
     print('Variance score: %.2f' % r2_score(Y_train, y_pred))
     plt.scatter(X_train, Y_train, color='blue', label='Datos')
     plt.plot(X_train, y_pred, color='red', label='Recta de regresión')
     plt.xlabel('X')
     plt.ylabel('Y')
     plt.title('Regresión Lineal')
     plt.legend()

# Mostrar gráfico
     plt.show()
     # Obtener todos los 'userid' únicos
     sns.set(style='whitegrid', context='notebook')
     cols = ["R_Grade","R_Grade"]
     print("jelou")
     examens.hist()
     plt.show()
     sns.pairplot(examens[cols], height=1.75);
     print("jelou2")
     
     #trameses prova

     '''trameses = trameses.fillna(0)
     x = trameses['grade'].values.reshape(-1, 1)
     y = trameses['userid'].values.reshape(-1, 1)
     X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=0)
     trameses = trameses.fillna(0)
     regressor = LinearRegression()
     regressor.fit(X_train, Y_train)
     y_pred = regressor.predict(X_train)
     print('Coefficients: \n', regressor.coef_)
     print('Independent term: \n', regressor.intercept_)
     print("Mean squared error: %.2f" % mean_squared_error(Y_train, y_pred))
     print('Variance score: %.2f' % r2_score(Y_train, y_pred))
     plt.scatter(X_train, Y_train, color='blue', label='Datos')
     plt.plot(X_train, y_pred, color='red', label='Recta de regresión')
     plt.xlabel('X')
     plt.ylabel('Y')
     plt.title('Regresión Lineal')
     plt.legend()

# Mostrar gráfico
     plt.show()
     # Obtener todos los 'userid' únicos
     user_ids = trameses['userid'].unique()
     sns.set(style='whitegrid', context='notebook')
     cols = ["userid","grade"]
     print("jelou")
     trameses.hist()
     plt.show()
     sns.pairplot(trameses[cols], height=1.75);
     print("jelou2")
     '''

prueba()