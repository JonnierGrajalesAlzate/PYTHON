def saludar(name):
    return(f"hola {name} bienvenido")
    
def saludo_mejorado(sexo, nombre):
    sexo = sexo.lower()
    if(sexo=="hombre"):
        adjetivo = "macho"
        return f"hola {nombre} eres un {adjetivo}"
    elif(sexo=="mujer"):
        adjetivo="femina"
        return f"hola {nombre} eres una {adjetivo}"
    else:
        adjetivo="raris"
        return f"hola {nombre} eres {adjetivo}"
    
print(__name__)