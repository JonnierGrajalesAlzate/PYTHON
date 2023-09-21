def suma():
    
    while True:
       a= input("numero1:  ")
       b= input("numero2:  ")
       try:
         resultado = int(a)+  int(b)
       except:
        print("te pedi un numero")
       else:
           break
       finally:#se ejecuta siempre
           print("manejo de excepción finalizado")
    return resultado

print(suma())