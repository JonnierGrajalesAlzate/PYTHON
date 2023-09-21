#creando diccionario con dict(), se puede crear diccionarios vacios 
diccionario = dict(nombre="jonnier", apellido="grajales", edad=17)

#crearlo de forma normal 
diccionario_normal = {
    "nombre": 'jonnier',
    "apellido": 'grajales',
    "edad": 17
}

#creando diccionario con dict.fromkeys() primer datos es un iterable 
#n=apellido 
#o=apellido 
#m=apellido 
#b= apellido 
#r= apellido 
#e= apellido
diccionario_from = dict.fromkeys(["nombre", "apellido"])
#obtener resultado de ese metodo con dict()
res = diccionario.get("nombre") 

#obtener resultado del diccionario_normal con get
res_2 = diccionario_normal.get("edad")
print(diccionario_from)