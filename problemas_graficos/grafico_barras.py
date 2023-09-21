import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("problemas_graficos\\notas.csv")
sueldo_total = df["sueldo"].sum()

#barplot es digrama de barras
sns.barplot(x="nombre",y="sueldo",data=df)
#mostrando con show()
plt.show()