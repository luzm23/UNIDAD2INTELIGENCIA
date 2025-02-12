import datetime

nombre=input("ingrese el nombre: ")
fecha = datetime.datetime.now().strfime("%Y-%m-%d %H:%M:%S")
print(f"nombre del cliente: {nombre} y la fecha  y hora: {fecha}")