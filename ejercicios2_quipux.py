from colorama import init
init(autoreset=True)

lista=[]
for i in range(3):
    nombre=input("NOMBRE:  ")
    edad = int(input("EDAD:  "))
    persona=(nombre,edad)
    lista.append(persona)
    lista.sort(key=lambda x:x[1])
    nombre = lista[-1][0]
    edad = lista[-1][1]
print("EL MAYOR DE TODOS ES:")
print("\033[93m"+f"{nombre} y tiene {edad} años")