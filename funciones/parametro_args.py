#forma no optima de sumar valores
#def suma(lista):
    #numeros_sumados =0
    #for numero in lista:
     #   numeros_sumados = numeros_sumados + numero
      #  return numeros_sumados

#utlizando el parametro args
#podemos usar *->(args) crea una lista
def suma(nombre, *numeros):#debemos de colccarlo al final si hay mas parametros
    return f"hola {nombre} la suma es: {sum(numeros)}"
res = suma("jonnier",3,6,2,8,4)

#otra forma de hacerlo, es colocar el args(*) en el return
def suma2(numeros):
    return sum([*numeros])
        
resultado = suma2([3,8,9,10])
print(resultado)
