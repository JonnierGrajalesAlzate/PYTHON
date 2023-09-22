print("escribe una frase con mas de 20 letras")
frase = input("Dame una frase:  ")
cantidad_de_palabras = len(frase)
tiempo_en_decirlas = cantidad_de_palabras/2

if cantidad_de_palabras < 20:
    print(f"FALLASTE TU PALABRA ES DE {cantidad_de_palabras} LETRAS")
    print(f"TE DEMORAS EN DECIRLA {tiempo_en_decirlas} SEGUNDOS")

else:
    print(f"FELICIDADES TU PALABRA ES DE {cantidad_de_palabras} LETRAS")
    print(f"TE DEMORARAS EN DECIRLA {tiempo_en_decirlas} SEGUNDOS")
    
