#creando una lista con list
lista = list([38,18,35,17,19,57,3])

#LEN es de longitud, cantidad de elementos en lista
resultado = len(lista)

#APPEND agregando un elemento a la lista
lista.append(23)

#INSERT agrega un elemento en un indice especifico, no borra datos
lista.insert(2, 18)

#EXTENDS agrega varios elementos a la lista, dentro de corchetes
lista.extend([2030])

#POP elimina un elemento de la lista por su indice
lista.pop(-1)#con el -1 eliminamos el último de la lista y asi sucesivamente

#REMOVE remueve un elemento por su valor
lista.remove(38)

#SORT  ordena una lista de forma descendente o ascendente pero solo con numeros
lista.sort()#con el reverse=True podemos cambiar el orden descendente

#REVERSE inviertiendo los elementos de una lista
lista.reverse()

#CLEAR elimina todos los elemntos de la lista
lista.clear()

