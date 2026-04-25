import csv
import os

ruta_archivo = os.path.join(os.path.expanduser("~"), "frutas.csv")

datos_frutas = []

with open(ruta_archivo, "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        datos_frutas.append(fila)

print(datos_frutas)
