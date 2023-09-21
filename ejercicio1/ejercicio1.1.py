#otros cursos y dalto
minimo = 2.5
promedio = 4
maximo = 7
curso_dalto = 1.5
crudo_otros =5
crudo_dalto = 3.5

#diferencias de duracion
diferencia_con_el_min = int(curso_dalto /minimo * 100)
diferencia_con_el_max = int(curso_dalto / maximo * 100)
diferencia_con_el_promedio = int(curso_dalto / promedio *100)
crudo_dalto_duracion = int(curso_dalto / crudo_dalto * 100)
crudo_otroscursos = int(promedio / crudo_otros * 100)
cantidad_de_cursos = int(10/ curso_dalto)


print(f"difrencia con el mas rapido = {diferencia_con_el_min}%")
print(f"difrencia con el mas lento = {diferencia_con_el_max}%")
print(f"difrencia con el promedio = {diferencia_con_el_promedio}%")
print(f"difrencia con el crudo dalto = {crudo_dalto_duracion}%")
print(f"difrencia con el crudo otros cursos = {crudo_otroscursos}%")
print(f"con 10 horas te puedes ver = {cantidad_de_cursos} de dalto")
