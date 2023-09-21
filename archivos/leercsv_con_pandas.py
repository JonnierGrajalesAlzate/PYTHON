#instale pandas con py -m pip install pandas en el "cmd" de windows
import pandas as pd
#df es dataframes que es como si fueran hojas de cálculo
df = pd.read_csv("archivos\\dato.csv")
df2 = pd.read_csv("archivos\\dato.csv")
nombre = df["nombre"]#para mostrar los nombres

#ordenandolo ascendente
d_ordenados_asc = df.sort_values("edad")#sort_values()es para ordenar el valor que queramos

#ordenandolo descente
#viene por defecto ordenado ascendentemente
d_ordenados_desc = df.sort_values("edad", ascending=False)#con el ascending=False

#concatenando los dos dataframes
df_concatenando = pd.concat([df,df2])#con el concat

#accediendo a la primeras filas con head() de arriba para abajo
primeras_filas= df.head(2)#nos muestra las primeras filas que queramos dependiendo el parametro

#accediendo a las ultimas filas con tail() abajo para arriba
ultimas_filas = df.tail(2)#nos muestras las ultimas filas dependiendo el parametro

#accediendo a la cantidad de filas y columnas con shape
rows_columns = df.shape#devuelve una tupla () el primer valor son las filas y el otro las columnas

rows = rows_columns[0]
columns = rows_columns[1]

#obteniendo data estadistica del dataframe:
df_info = df.describe()

#accediendo a un elemento especifico con loc
elemento_especifico = df.loc[2, "edad"]#24

#accediendo con los indices con iloc la i es de indice
elemento_especifico2 = df.iloc[2, 2]#24


#accediendo a todos lo apelldios de una columna
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3= df.loc[2,:]

#accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"]<30,:]
print(mayor_que_30) 