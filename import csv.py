import csv

with open(r'C:\Users\cetecom\Documents\listadoRutEmpresa_cargo.csv', 'r', newline = "") as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv, delimiter = ";")
    for fila in lector_csv:
        if int(fila ['ventas']) <= 100000000:
            print(f"La empresa{fila['nombre']} es un Pequeño contribuyente ")

        if 100000001 < int(fila ['ventas']) <= 200000000:
            print(f"La empresa{fila['nombre']} es un Mediano contribuyente ")

        if int(fila['ventas']) <= 200000000:
            print(f"La empresa{fila['nombre']} es un Gran contribuyente ")