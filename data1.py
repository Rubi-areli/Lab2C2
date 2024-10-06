"""https://www.kaggle.com/datasets/ironwolf404/electric-vehicle-population-in-usa"""

"""Este gráfico muestra la distribución de vehículos eléctricos según la marca de los autos."""
# llamamos las librerias
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('auto.csv', encoding='latin1')

# Agrupar por marca de vehículo (Make) y contar
data_by_make = df.groupby('Make').size().sort_values()

# Generar el gráfico de barras
plt.bar(data_by_make.index, data_by_make.values)

# Etiquetas y título
plt.ylabel('Número de Vehículos')
plt.xlabel('Marca')
plt.title('Distribución de Vehículos Eléctricos por Marca')

# Rotar las etiquetas para mayor claridad
plt.xticks(rotation=90)

# Ajustar el layout y mostrar el gráfico
plt.tight_layout()
plt.show()

