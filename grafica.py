from colorama import init
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
init(autoreset=True)

df = pd.read_csv("lista.csv")
sns.barplot(x="nombre",y="dinero",data=df)
plt.show()
dinero_total = df["dinero"].sum()
print("\033[96m"+f"En total todos tienen: ${dinero_total} Pesos")