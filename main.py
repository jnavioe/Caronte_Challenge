import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from src.modules.Predictor import Predictor
from src.modules.StudentProcessor import StudentProcessor


def main(test_size=0.8, random_state=42):
    students = StudentProcessor().process()
    totalPrediction = []
    totalGrade = []
    df_model = pd.DataFrame([student.statics() for student in students])

    features = ['n_submissions', 'mean_submissions', 'exam_midterm', 'exam_final', 'exam_makeup', 'n_tried']
    x = df_model[features].copy()
    x[['exam_midterm', 'exam_makeup']] = x[['exam_midterm', 'exam_makeup']].fillna(0)
    y = df_model['final_grade']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=random_state)

    predictor = Predictor()
    predictor.train(students, x_train, y_train)

    try:
        result = []
        error_abs = []
        for (_, student), grade in zip(x_test.iterrows(), y_test):
            prediction = predictor.predict(pd.DataFrame([student]))
            result.append([prediction, grade])
            error_abs.append(np.abs(prediction - grade))
            totalPrediction.append(prediction)
            totalGrade.append(grade)
            print("Prediccion:", prediction, "; Grade;", grade)

        print(f"Error absoluto - Media: {np.mean(error_abs):.2f}; Máximo: {np.max(error_abs):.2f}; Desviación estándar: {np.std(error_abs):.2f}")
        plt.figure(figsize=(10, 5))
        plt.scatter(totalPrediction, totalGrade, color='blue', marker='o', s=100)
        plt.title("notas")
        plt.xlabel("Predicción")
        plt.ylabel("Notas reales")

# Mostrar el gráfico
        plt.show()
    except:
        predictions = np.array([predictor.predict(pd.DataFrame([row])) for _, row in x_test.iterrows()])
        

if __name__ == "__main__":
    main()
