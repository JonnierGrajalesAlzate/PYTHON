from colorama import init
init(autoreset=True)

def cantidad_amigos(cantidad):
    lista = []
    for i in range(cantidad):
        nombre = input("NOMBRE:  ")
        edad = int(input("EDAD:  "))
        compa = (nombre, edad)
        lista.append(compa)
    lista.sort(key=lambda x:x[1])
    mayor_nombre = lista[-1][0]
    mayor_edad = lista[-1][1]
    menor_nombre =lista[0][0]
    menor_edad =lista[0][1]
    return mayor_nombre,mayor_edad,menor_nombre,menor_edad,lista

mayor_nombre,mayor_edad,menor_nombre,menor_edad,lista=cantidad_amigos(4)
print("\033[96m"+ f"lista:  {lista}")
print("\033[93m"+ f"NOMBRE DEL MAYOR: {mayor_nombre}")
print("\033[93m"+ f"EDAD DEL MAYOR: {mayor_edad}")
print("\033[92m"+ f"NOMBRE DEL MENOR: {menor_nombre}")
print("\033[92m"+ f"NOMBRE DEL MENOR: {menor_edad}")

    