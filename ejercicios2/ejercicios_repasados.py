#numeros pares e impares
#numeros=[1,2,3,4,5,6,7,8,9,10]
#def es_par(numeros):
#    pares=[]
#    impares=[]
#    for numero in numeros:
#        if(numero%2==0):
#            pares.append(numero)
#        else:
#            impares.append(numero)
#    return pares,impares

#pares,impares = es_par(numeros)

#alumno_mayor, alumno menor

#def cantidad_alumnos(cantidad):
#    alumnos = []
#    for i in range(cantidad):
#        nombre=input("Nombre:  ")
#        edad=int(input("Edad: "))
#        alumno = (nombre, edad)
#        alumnos.append(alumno)
#    alumnos.sort(key=lambda x:x[1])
#    mayor_nombre = alumnos[-1][0]
#    mayor_edad = alumnos[-1][1]
#    menor_nombre = alumnos[0][0]
#    menor_edad = alumnos[0][1]
#    return mayor_nombre, mayor_edad, menor_nombre,menor_edad

#mayor_n, mayor_e, menor_n, menor_e = cantidad_alumnos(3)

#primo
#def numeros(num):
#    for i in range(2, num):
#        if(num%i==0):
#            return False
#    return True

#def numeros_primos(num):
#    primos=[]
#    for i in range(2, num):
#      if numeros(i)==True:
#          primos.append(i)
#    return primos

#res = numeros_primos(19)
#print(res)
    
#fibonacci
#def fibonaccio(num):
#    n_generados=[]
#    a,b=0,1
#    for i in range(1, num+1):
#        n_generados.append(a)
#        a,b =b, a+b
#    return n_generados

#res = fibonaccio(8)
#print(res)
    