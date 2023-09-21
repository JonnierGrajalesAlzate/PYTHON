import seaborn as sns
import matplotlib.pyplot as plt

porcentaje = [20,15,15,25,12,3,10]#lista con los porcentaje
colores = sns.color_palette("dark")#sns proporciona una paleta de colores 
plt.pie(porcentaje,colors=colores)#pir es para asignarle que va a ser diagrama redondo
plt.show()#muestra grafico circular