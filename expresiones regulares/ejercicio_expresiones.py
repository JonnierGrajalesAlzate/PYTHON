import re
texto = "El número de jonnier es +57 302 415 8318 contactalo"

padre = r"\+\d{2}\s\d{3}\s\d{3}\s\d{4}"


res = re.sub(padre,"numero oculto",texto)
print(res)