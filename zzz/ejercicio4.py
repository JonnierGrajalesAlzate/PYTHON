from colorama import init
init(autoreset=True)

def cantidad_numeros (cantidad):
    lista = []
    for i in range(cantidad):
        numero = int(input(f"Numero {i+1}:  "))
        lista.append(numero)
    lista.sort()
    print(f"LISTA= {lista}")
    res = sum(lista)
    print("\033[93m" + f"la suma es: {res}")

cantidad_numeros(4)
    