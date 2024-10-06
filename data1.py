"""https://www.kaggle.com/datasets/vikasukani/diabetes-data-set"""

"""BloodPressure: Esta columna contiene los valores de presión sanguínea de cada persona.
Outcome: Esta columna indica si una persona tiene diabetes (1) o no (0).
Agrupación: El código agrupa los datos por el valor de Outcome y luego calcula el promedio
 de la presión sanguínea para cada grupo.
Gráfico de barras: Muestra el promedio de presión sanguínea para personas con y sin diabetes."""

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("diabetes-dataset.csv")

# Agrupar por Outcome (0 = No diabetes, 1 = Con diabetes) y calcular el promedio de presión sanguínea
average_blood_pressure = df.groupby('Outcome')['BloodPressure'].mean()

# Generar el gráfico de barras para la presión sanguínea
plt.bar(average_blood_pressure.index, average_blood_pressure.values, color=['#FF9999', '#66B3FF'])

# Etiquetas y título
plt.xticks([0, 1], ['No tiene diabetes', 'Tiene diabetes'])
plt.ylabel('Promedio de Presión Sanguínea')
plt.title('Promedio de Presión Sanguínea en Pacientes con y sin Diabetes')

# Mostrar el gráfico
plt.show()

