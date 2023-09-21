import re

texto = '''mes jonnier. mi capitan como estas?
esta Linea es la 6 .segunda 201 linea de 12 texto 2. 
y Esta es la tercera. 1 linea de 2 código'''

#devuelve el resultado de minusculas y mayusculas dependiendo la palabra a encontrar
resultado_finall_flags = re.findall("linea",texto,flags=re.IGNORECASE)
resultado_finall = re.findall("linea", texto)#encuentra todos los valores de la variable#devuelve una lista
resultado_search = re.search("hola",texto)#el primero es la palabra a encontrar y el otro la variable

#\d ->busca digitos numericos del 0 al 9
#\D ->busca TODO menos los digitos numeros del 0 al 9
#con la r"" indicamos que vamos a utilizar expresiones regulares
resultado_d = re.findall(r"\d",texto)#devuelve una lista con los numeros encontrados
resultado_D = re.findall(r"\D",texto)#devuelve cada letra de la cadena menos numeros

#\w ->busca carácteres alfanúmericos
#\W ->busca TODO menos los carácteres alfanúmericos
resultado_w= re.findall(r"\w",texto)#devuelve alfanúmericos 
resultado_W= re.findall(r"\W",texto)#no devuelve alfanúmericos como ","" ","\n"

#\s -> busca espación en blanco y saltos de linea
resultado_s = re.findall(r"\s",texto)#devuelve " ", "/n"
resultado_S = re.findall(r"\S",texto)#devuelve lo demás que no sea espacios ni saltos

#\. -> busca TODO menos saltos de linea
#\n -> busca TODO los saltos en linea
resultado_punto = re.findall(r"\.",texto)
resultado_saltos = re.findall(r"\n",texto)

#\ -> cancelamos carácteres especiales
resultados_guion_bajo = re.findall(r"\.", texto)#cancelando la función del punto y buscando puntos

#armando un texto que busque un número, seguido de un punto y un espacio
nueva_cadena = re.findall(r'\d\.\s',texto)#buscamos el conjunto de todo esto

#buscar el principio de una linea (^)
principio = re.findall(f'^mes',texto)

#buscar el final de una linea ($)
final = re.findall(f'código$',texto)

#{n} busca n cantidad de veces el valor de la izquierda
conjunto = re.findall(r'\d{3}',texto)#encontrame {3} numeros

#{n,m} almenos n, como máximo m
rango = re.findall(r'\d{1,3}', texto)#devuelve los numeros que por lo menos tenga 1 y por lo maximo3
print(conjunto)
