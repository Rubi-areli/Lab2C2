"""https://www.kaggle.com/datasets/niharika41298/nutrition-details-for-most-common-foods

Vamos a hacer un gráfico de líneas que compare las calorías de varios tipos de alimentos. 
Usaremos las columnas Food alimento y Calories calorías"""
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset de nutrientes
df = pd.read_csv('nutrients_csvfile.csv')

# Seleccionar algunas columnas: alimentos y calorías
df_selected = df[['Food', 'Calories']]

# Ordenar los datos por el valor de calorías
df_sorted = df_selected.sort_values(by='Calories', ascending=False).head(20)  # Tomamos los 20 alimentos con más calorías

# Generar el gráfico de líneas
plt.plot(df_sorted['Food'], df_sorted['Calories'], marker='o')

# Etiquetas y título
plt.ylabel('Calorías')
plt.xlabel('Alimentos')
plt.title('Calorías por Alimento (Top 20)')

# Rotar las etiquetas del eje x para mejor legibilidad
plt.xticks(rotation=90)

# Ajustar el layout y mostrar el gráfico
plt.tight_layout()
plt.show()
