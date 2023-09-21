#creando una funcion de tres parametros
#def frase(nombre, apellido, adjetivo):
#    return f"hola {nombre} {apellido} eres {adjetivo}"
#utilizando keyword arguments
#frase_resultante =  frase(adjetivo="jonnier",nombre= "grajales", apellido="pinta")
#print(frase_resultante)

#se puede definir el valor del parametro hay mismo pero queda de manera forzado ya que es opcional
def saludo(nombre, apellido, adjetivo = "crack"):
    return f"hola {nombre}{apellido} eres {adjetivo}"

res = saludo("jonnier", "grajales", "proplayer")#aqui le coloque otro valor al adjetivo al ser opcional
print(res)