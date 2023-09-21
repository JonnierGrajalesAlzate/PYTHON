#te dan la lista del 1 al 10 
#clasifica los numeros pares e impares
#proceso: primero defini dos funciones lambda en donde tenian como argumento numero 
#dependiendo si este daba como resultado 0 o 1 ya se determinaba si era par o impar
#depués cree dos variables en las que utilice el filter() en donde como primer parametro
#coloque la funcion correspondiente que daba como resultado "true" y en el otro parametro
#coloque la lista del 1 al 10
#por ultimo hice dos impresiones una que convertia una list() de números pares y otra impares
numeros_pares = lambda numero: numero%2==0
numeros_impares = lambda numero: numero%2==1

numeros = [1,2,3,4,5,6,7,8,9,10]

pares = filter(numeros_pares,numeros)
impares = filter(numeros_impares,numeros)

print(f"los numero de la lista son {numeros}")
print(f"pares: {list(pares)}")
print(f"impares: {list(impares)}")