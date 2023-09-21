nombre= input("dime tu nombre: ")
frase = input("dame un frase: ")
palabras_por_segundo = 2
palabra_desglosada = frase.split(" ")
cantidad_de_palbras = len(palabra_desglosada)
tiempo = cantidad_de_palbras/palabras_por_segundo
tiempo_dalto = cantidad_de_palbras/palabras_por_segundo/3
print(f"dalto se demora en decirla {tiempo_dalto}")

if(cantidad_de_palbras<120):
    print(f"la cantidad de palabras son {cantidad_de_palbras} y te demoraste {tiempo} segundos")
else:
    print(f"{nombre} te demoraste {tiempo} y lo minimo era 60s")
