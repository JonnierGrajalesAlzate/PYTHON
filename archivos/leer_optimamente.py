#Abriendo el archivo con With Open
with open("archivos\\texto_jonnier.txt", encoding="UTF-8") as archivo:
    #Leemos el archivo
    contenido = archivo.read()
    
    #imprimimos el resultado
    print(contenido)
#no es necesario usar el Close al usar WithOpen
    