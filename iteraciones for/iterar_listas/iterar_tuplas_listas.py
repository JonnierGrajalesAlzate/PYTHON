animales = ["perro", "gato", "perico", "pez", "toro"]
numeros = [1,4,2,5,7]
#el for __ in   : en para recorrer la lista ya creada
#lista con letras
for animal in animales:
    print(f"{animal}")
#lista con numeros
for numero in numeros:
    print(numero * 10)
    
#misma cantidad de elementos en ambas listas para hacer lo siguiente zip()
#se itera al mismo tiempo
for numero,animal in zip(animales, numeros):
   print(f"recorriendo la lista1 {numero}")
   print(f"recorriendo la lista2 {animal}")
    
#metodo range(5, 29) primero es en donde arranca y el otro en donde termina
#con un solo parametro arranca desde el cero hasta el valor del parametro
for numero in range(3):
    print(numero)

#forma de recorrer una lista con su indice con enumerate()
#devuelve una dupla con (indece valor)
#parecido a forEach
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es {indice} y el valor es {valor}")

#usando el for/else 
for numero in numeros:
    print(numero)
else:
    print("el bucle termino")
    
#todo funciona igual para las tuplas y listas