from colorama import init
from itertools import permutations
init(autoreset=True)
digitos = "0123"

permutacion = ["".join(p) for p in permutations(digitos)]
contador = 0

for p in permutacion:
    print("\033[94m" + p)
    contador+=1

print("\033[93m" + f"hay {contador} casos posibles")