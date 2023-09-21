#creando una funcion que nos devuelva los números primos 
#entre 0 y el numero que pasamos

def es_primo(num):#defino la primera función para saber si es numero primo
    for i in range(2, num-1):#el rango comienza desde 2 ya que el 0 y el 1 no son primos
        if(num%i ==0): return False#si num%cada iteracion ==0 que retorne falso
    return True#de lo contrario que retorne verdadero ya que el primo es el que solo tiene dos divisores

def lista_primos(num):#se crea otra lista  para adjuntar los numero primos dependiendo el rango que nos de el usuario
    primos = list()#esta es la lista en donde se guardaran los valores primos
    for i in range(2, num+1):#el +1 es para que me genere el ultimo en caso de que lo haya
        resultado = es_primo(i)#el resultado va a ser igual a lo que nos retone la otra funcion "es_primo"
        if resultado == True:#si la función pasada daba True que se guarde en la lista "primos"
            primos.append(i)
    return primos#al final retornara la lista de primos 

res = lista_primos(98)
print(res)   
            
    