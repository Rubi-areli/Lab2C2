"""https://www.kaggle.com/datasets/vikasukani/diabetes-data-set"""

"""El gráfico de barras muestra la cantidad de personas en el dataset clasificadas según si tienen 
o no diabetes, basado en la columna Outcome. Los dos grupos representados son:

Personas sin diabetes (Outcome = 0): Este grupo corresponde a las personas que no tienen diabetes.
Personas con diabetes (Outcome = 1): Este grupo incluye a las personas que han sido diagnosticadas con diabetes."""

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("diabetes-dataset.csv")

# Contar cuántas personas tienen y no tienen diabetes
data_by_outcome = df['Outcome'].value_counts()

# Generar el gráfico de barras
plt.bar(data_by_outcome.index, data_by_outcome.values, color=['#FF9999', '#66B3FF'])

# Etiquetas y título
plt.xticks([0, 1], ['No tiene diabetes', 'Tiene diabetes'])
plt.ylabel('Cantidad de personas')
plt.title('Distribución de Pacientes con y sin Diabetes')

# Mostrar el gráfico
plt.show()

