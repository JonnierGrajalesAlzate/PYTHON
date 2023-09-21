import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("ejercicios_cofla\\cofla_ingresos.csv")
#BARPLOP es digrama de barras
sns.barplot(x="fuente", y="ingresos", data=df)

#obteniendo el total de ingresos 
total_ingresos = df['ingresos'].sum()
#mostrando el total
print(f"el total de ingresos es: {total_ingresos}")
plt.show()