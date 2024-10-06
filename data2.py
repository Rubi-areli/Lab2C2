"""https://www.kaggle.com/datasets/jeffreybraun/chipotle-locations
el dataset de Chipotle Locations visualizamos la distribución de las ubicaciones por estado. """
import pandas as pd
import matplotlib.pyplot as plt

# dataset de Chipotle
df = pd.read_csv('chipotle_stores.csv', encoding='latin1')

# Agrupamos por estado y contar las ubicaciones de Chipotle por cada uno
data_by_state = df['state'].value_counts()

# tuvimos que agrupar los estados con pocos restaurantes en 'Otros' porque los dtos que hay son demasiados
threshold = 50  # agrupamos estados con menos de 50 restaurantes
data_grouped = data_by_state[data_by_state >= threshold]
data_grouped['Otros'] = data_by_state[data_by_state < threshold].sum()

# utiliuzamos colores personalizados para el gráfico circular
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ff6666','#c2c2f0','#ffb3e6','#c2f0c2','#c2f0c3']

# Generarmoo el gráfico circular
plt.pie(data_grouped.values, labels=data_grouped.index, colors=colors, autopct='%1.1f%%')

# Añadirmos un título
plt.title('Distribución de Restaurantes Chipotle por Estado')

# Mostrar
plt.tight_layout()
plt.show()

# Agrupación por estado: Se agrupan las ubicaciones de Chipotle por estado usando value_counts(), lo que te dará la cantidad de restaurantes en cada estado.
# Colores personalizados: Definí una lista de colores variados para las porciones del gráfico.
# Gráfico circular: Se genera el gráfico utilizando los valores y etiquetas de los estados.