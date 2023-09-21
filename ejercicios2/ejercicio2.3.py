#Ejercicio 2.2 Mejorado
def cantidad_alumnos(cantidad):
    alumnos = list()
    for i in range(cantidad):
        nombre = input("Nombre: ")
        edad = int(input("Edad:  "))
        alumno = (nombre, edad)
        alumnos.append(alumno)
    alumnos.sort(key=lambda x:x[1])
    profe_nombre = alumnos[-1][0]
    profe_edad = alumnos[-1][1]
    asistente_edad = alumnos[0][1]
    asistente_nombre = alumnos[0][0]
    return profe_nombre,profe_edad,asistente_nombre,asistente_edad

profe_nombre,profe_edad,asistente_nombre,asistente_edad = cantidad_alumnos(4)
print(f"Nombre del Profe: {profe_nombre}")
print(f"Edad del profe: {profe_edad}")
print(f"Nombre del Asistente: {asistente_nombre}")
print(f"Edad del Asistente: {asistente_edad}")