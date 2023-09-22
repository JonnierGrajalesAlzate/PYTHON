from colorama import init
init(autoreset=True)

class colores:
    Verde= '\033[92m'
    Amarillo = '\033[93m'
    Rojo = '\033[91m'
    Reset = '\033[0m'

numeros_pares = []
numeros_impares = []
numeros = []
for i in range(1,6):
    numero = int(input(f"Numero {i}:  "))
    numeros.append(numero)
print(f"lista generada:{numeros}")

for numero in numeros:
    if numero%2==0:
        numeros_pares.append(numero)
        numeros_pares.sort()
    else:
        numeros_impares.append(numero)
        numeros_impares.sort()
print(colores.Verde + f"PARES = {numeros_pares}"+ colores.Reset)
print(colores.Rojo + f"IMPARES = {numeros_impares}"+ colores.Reset)

