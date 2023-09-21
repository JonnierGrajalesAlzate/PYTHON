#encontrando el numero mayor de una lista
numeros = [5,2,6,3,1]
#max es de maximo para encontrar el numero mayor
#min es de minimo  para encontrar el numero menor
numero_mayor= max(numeros)#6
numero_menor = min(numeros)#1


#redondeando a 6 decimales con el round(numero, decimales que les queres dejar)
numero_a_redondear =6.62193473
numero_redondeado = round(numero_a_redondear,3)#6.622

#bool() retorna Flase-> 0, vacio, False, ninguno
res = bool()#false
res2= bool(-1)#true

#all() retorna true si todos los valores son verdaderos
resultado_all = all([234, "jonnier", [345,45]])#true 0=false

#sum() suma todos los valores de un iterable
edades =[17,38,31,28]
suma_edades = sum(edades)#114