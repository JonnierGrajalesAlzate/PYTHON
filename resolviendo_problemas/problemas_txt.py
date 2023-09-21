#2 listas, una con nombre otra con apellidos

nombres = ["Jonnier","Juan", "Yeferson"]
apellidos = ["Grajales", "Zapata", "Grajales"]
edades = [17,22,12]

#registrar esta informacion en un txt en una forma optima

with open("resolviendo_problemas\\nombres_y_apellidos.txt","w") as archivo:
    archivo.writelines("[Los datos generados son:] \n")
    for nombre,apellido,edad in zip(nombres, apellidos,edades):
        archivo.writelines(f"{nombre} {apellido} {edad} \n")
    