#w->write(escribir "sobreescribe")  a->append(agregar"repite cada vez se ejecute")
#con la "w" y "a" es append hace lo mismo tenemos el permiso de escribir en un archivo 
with open("archivos\\texto_jonnier.txt","w",encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("Nuevo texto")
    #agregando dos lineas con writelines()
    archivo.writelines(["Hola maestro como andas \n", "misericordia"])#\n es para salto de linea
    
    