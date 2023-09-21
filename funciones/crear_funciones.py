#def es una funcion se necesita de (parametros)
def saludar(nombre):
    print(f"hola {nombre} bienvenido")
saludar("Jonnier")#hola jonnier bienvenido

#def con varios parametros
def saludo2(nombre, edad):
    print(f"hola {nombre} tu edad es {edad} años")
#hola jonnier tu edad es 17 años

#def con condiones
def persona_saludo(sexo, nombre):
    sexo = sexo.lower()#para convertirlo en minúscula
    if(sexo=="mujer"):
        print(f"hola {nombre} eres {sexo}")
    else:
        print(f"hola {nombre} eres {sexo}")

persona_saludo("Mujer", "erika")
persona_saludo("hombre", "jonnier")

#crear una funcion que nos retorne valores 
def password(num):
    chars = "abcdefghijk"
    numero_entero = str(num)
    num = int(numero_entero[0])#para que me agarre el primer numero de ese str
    c1 = num -2
    c2 = num
    c3 = num - 6
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña, num
    
contra, numeroU = password(92)#desempaquetado
print(f"el numero utilizado fue {numeroU}")
print(f"tu nueva contraseña es {contra}")