import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pl

df = pd.read_csv("z\\pizzas.csv") 
sns.lineplot(x="fecha", y="pizzas", data=df)
pl.plot("03-02", 5, "o")
pl.show()