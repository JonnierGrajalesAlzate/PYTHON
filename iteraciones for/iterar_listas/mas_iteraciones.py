personas = ["jonnier", "yeferson", "viejorro", "erika"]

vueltas = 0
#iteracion con continue
for persona in personas:
    vueltas += 1
    if(persona == "viejorro"):
        continue
    print(f"persona{vueltas} es: {persona}")

#iteraciones con break
for persona in personas:
    vueltas += 1
    if(persona == "viejorro"):
        break
    print(f"persona{vueltas} es: {persona}")

#recorrer una cadena de texto
cadena = "hola jonnier"

for letra in cadena:
    print(letra)
    
#for en una sola linea de código forma rapida
numeros =[2,5,8,10]
numeros_duplicados = [n*2 for n in numeros]
print(numeros_duplicados)

#for de forma lenta con esta misma lista pero queda de la misma manera
numeros_dplicados = list()
for numeroo in numeros:
    numeros_dplicados.append(numeroo*2)
print(numeros_dplicados)