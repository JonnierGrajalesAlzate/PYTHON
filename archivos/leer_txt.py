#open("")es para abrir un archivo.txt y el Read() es para leerlo
#El encoding es para colocarle el UTF-8 para que sea universal
#Asi reconocerá comas, tildes etc
archivo_abierto = open("archivos\\texto_jonnier.txt", encoding="UTF-8")
#leer archivo completo
#archivo_leido = archivo_abierto.read()

#leer linea por linea
#lineas = archivo_abierto.readlines()

#leer una sola linea
linea = archivo_abierto.readline()#en el parametro podemos podes cuantos caracteres leer
#cerrar el archivo
archivo_abierto.close()
print(linea)