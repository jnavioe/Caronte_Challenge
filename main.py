from src.entity.submission import Submission
from src.entity.activity import Activity
from src.entity.exam import Exam
from src.CSV.csv import CsvReader
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


CSV_DIR = "/home/toni/Caronte_Challenge/src/entity/activity.py"

def prova():
    # Cargar los archivos CSV
     trameses = pd.read_csv('./public/trameses.csv')
     activitats = pd.read_csv('./public/activitats.csv')
     examens = pd.read_csv('./public/notes.csv', delimiter=';')

     # Obtener todos los 'userid' únicos
     user_ids = trameses['userid'].unique()

     # Iterar sobre cada 'userid' y contar trameses y exàmens
     for user_id in user_ids:
          # Filtrar los trameses por el 'userid'
          trameses_filtrados = trameses[trameses['userid'] == user_id]


          tramesesObj = []
          # Objectes trameses
          for tramesa in trameses_filtrados.values:
               
               id=tramesa[0]
               fechasubida=tramesa[3]
               nota=tramesa[7]
               fechaNota=tramesa[5]
               n_intentos=tramesa[7]
               print(id)
               print(fechasubida)

               tramesesObj.append(Submission(id,fechasubida,nota,fechaNota,n_intentos)) 

          if trameses_filtrados.shape[0]==0:
               continue
          # Inicializar la lista de actividades filtradas
          activitats_filtrades = pd.DataFrame()  # Crear un DataFrame vacío por defecto
          
          # Filtrar las actividades asociadas a los trameses filtrados
          activitat_ids = trameses_filtrados['activitat_id'].unique()
          activitats_filtrades = activitats[activitats['activitat_id'].isin(activitat_ids)]

          # Contar el número total de exàmens
          total_examenes = activitats_filtrades



          # Activitat objectes

          activitatsObj = []
          for activitat in activitats_filtrades.values:
               
               id=activitat[0]
               nom=activitat[1]
               aulaId=activitat[2]
               dataInici=activitat[3]
               dataFinal=activitat[4]
               notaMax=activitat[5]
               activitatsObj.append(Activity(id,nom,aulaId,dataInici,dataFinal, notaMax,tramesesObj))
          
          # examens
          examens_filtrados = examens[examens['userid'] == user_id]
          examensObj = []
          #for exam in examens_filtrados:
            for exa in examens_filtrados.values:
              aulaId=exa[1]
              grade=exa[1]
              aulaId=exa[1]
              


              
               
             
          



          # Alumne objectes
          

          # Imprimir los resultados para cada alumno
          print(f"Alumno ID: {user_id}")
          print(f"Número total de exàmens: {total_examenes}")
          print('---')  # Separador para mayor claridad

           




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

