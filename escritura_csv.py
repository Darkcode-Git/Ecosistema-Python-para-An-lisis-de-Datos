import csv
import os

frutas = [
    ["Manzana", "Roja", "Dulce"],
    ["Plátano", "Amarillo", "Dulce"],
    ["Lima", "Verde", "Ácida"],
]

ruta_archivo = os.path.join(os.path.expanduser("~"), "frutas.csv")

with open(ruta_archivo, "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(frutas)

print(f"Archivo '{ruta_archivo}' creado exitosamente con {len(frutas)} filas.")
