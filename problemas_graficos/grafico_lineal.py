import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("problemas_graficos\\pedos.csv")
#creando un grafico 
sns.lineplot(x="fecha", y="pedos",data = df)

#creando un punto mas alto del grafico
plt.plot("07-07",12,"o")

#mostrando el grafico
plt.show()