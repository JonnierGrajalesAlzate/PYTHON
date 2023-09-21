#Todos los archivos que terminan en .py son modulos
#Tipos de Módulos:
#PythonModules, creados por python en C
#ModulosDeTerceros modulo de alguien mas que ya lo creo
#ModulosPropios creados por nosotros mismos

#para importar todo es asi pero es una mala práctica:
#from modulo_saludar import *


#import modulo_saludar as m_saludar
#asignarle otros nombre con "as" nombre que queramos
#saludo = m_saludar.saludar("jonnier")

#pero si solo queremos traer una funcion de otro archivo es asi:
#from modulo_saludar import saludar #(se importa1)
from modulo_saludar import saludar as saludo_jonni,saludo_mejorado #(se importan varios)
saludo= saludo_jonni("jonnier")
#print(saludo)
saludo2 = saludo_mejorado("hombre", "Jonnier")
#print(saludo2, saludo)

#accedemos al nombre de este modulo
#print(__name__)

#accedemos al nombre del modulo llamado
#print(saludo_jonni.__name__)