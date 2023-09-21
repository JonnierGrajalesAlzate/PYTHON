import csv

with open("archivos\\dato.csv") as archivo:
    reader = csv.reader(archivo)
    
    for fila in reader:
        print(fila)