#es como una funcion flecha en js (lambda) es una palabra clave
#es una funcion anonima que se pueden almacenar en variables

#sin lambda:
def multiplicar_por_dois (x):
     return x*2
res = multiplicar_por_dois(4)
#print(res)
 
 #con lambda hacemos lo mismo en pocas lineas pero no es optimo con varios parametro
multiplicar_por_dos = lambda x : x*2
#print(multiplicar_por_dos(5))

#usando filter con una funcion comun
#creando funcion comun que diga si es par o no
numeros =[1,2,3,4,5,6,7,8,9]

def par_impar(num):
    if(num%2==0):
        return True#tiene que devolver True para que filter actue
    else:
        return False
    
numeros_par = filter(par_impar, numeros)
#print(f"los numeros pares son: {list(numeros_par)}")

#creando lo mismo con una funcion lambda
numeros_pares = filter(lambda numero:numero%2==0,numeros)# aca directamente retorna true
#print(list(numeros_pares))
