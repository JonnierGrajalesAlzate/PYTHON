diccionario = {
    "nombre": 'jonnier',
    "apellido": 'grajales',
    "estado": 'soltero'
}

#con items() recorremos diccionario para obtener la clave y el valor
for key in diccionario.items():
    clave = key[0]
    valor = key[1]
    print(f"la calve es {clave} y el valor es: {valor}")