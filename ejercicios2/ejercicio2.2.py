#Hoy falto el profesor de clases entonces los jóvenes tuvierón una idea:
#Un alumno va a ser el profesor
#Un alumno va a ser su asistente
#A) Pedir el nombre y la edad de los compañeros que vinieron hoy a clase
#ordenar los datos de mayor a menor
#B)El mayor de la clase es el profesor y el menor es el asistente

#funcion para obtener la cantidad de alumnos
def cantidad_alumnos(cantidad):
  alumnos = list()#lista vacia para adjuntar los alumnos
  for i in range(cantidad):#bucle que pida nombre y edad a los alumnos
    nombre = input("Nombre:  ")
    edad = int(input("Edad:  "))
    alumno = (nombre, edad)#tupla en donde se guardarán los valores de cada alumno
    alumnos.append(alumno)#se añaden a la lista las tuplas asignadas
  alumnos.sort(key=lambda x:x[1])#función lambda para ordenar con sort() las edad
  profe=alumnos[-1][0]#[-1] es porque la edad mayor queda en ultima posión y el [0] es para el nombre
  asistente=alumnos[0][0]#[0] es porque la edad menor que queda ordenada de 1ro y el [0] es para el nombre
  return profe, asistente# retornara el profesor y el asistente

profe,asistente = cantidad_alumnos(4)#decimos que profesor y asistente van a ser iguales a la funcion principal
print(f"Profe={profe}")
print(f"Asistente={asistente}")