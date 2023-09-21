#algunos ejemplos de lo aprendido
#yeo tiene 4opciones para comprar una moto, pero una no le gusta

motos = ["Bóxer", "YZ", "Nmax", "Special"]
motos_nombre = [m for m in motos]
print(motos_nombre)
moto_borrada = input("¿Yeo cual no te gusta?")
print("opciones de compra:")
for moto in motos:
    if(moto == moto_borrada):
        continue
    
    print(moto)

mensaje = input("¿estas de acuerdo?")
if(mensaje == "Si"):
    print("Melo")
else:
    print("Que mal")