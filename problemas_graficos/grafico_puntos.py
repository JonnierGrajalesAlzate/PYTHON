import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("problemas_graficos\\titeres.csv")
#catplot es para hacer un diagrama de puntos
sns.catplot(x="nombre",y="porcentaje",data=df)
plt.show()