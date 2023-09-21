#cambiar el tipo de dato de una columna
import pandas as pd

with open("resolviendo_problemas\\datos.csv", encoding="UTF-8") as archivo:
    df = pd.read_csv(archivo)
    print(df)
    df['edad']=df['edad'].astype(str)#de esta manera se cambia el tipo de dato
    print(type(df['edad'][0]))
    
    df = df.dropna()#elimina las filas con datos faltantes NaN
    
    #eliminando filas repetidas drop_duplicates()
    df = df.drop_duplicates()#si las filas estan repetidas hay se eliminan
    
    #creando un dataframe con el dato resultante(limpio)
    
    #to_csv es para crear un archivo en donde esten las mejoras
    df.to_csv("resolviendo_problemas\\datos_limpios.csv")
    print(df)
    
    
    