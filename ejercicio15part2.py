import datetime
import random


nombre_tienda = "Tienda oxxo"
folio = random.randint(1000, 9999)
fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
nombre = input("Ingresa tu nombre: ")
producto = input("Ingresa el nombre del producto: ")
precio = float(input("Ingresa el precio unitario del producto: "))
cantidad = int(input("Ingresa la cantidad: "))
total_compra = precio * cantidad
descuento = total_compra * 0.10 if total_compra > 100 else 0
total_final = total_compra - descuento


print("\n" + "="*30 + " TICKET DE COMPRA " + "="*30)
print(f"Tienda: {nombre_tienda}")
print(f"Folio: {folio}")
print(f"Fecha y hora: {fecha_hora}")
print("-"*70)
print(f"Cliente: {nombre}")
print(f"Producto: {producto}")
print(f"Total de la compra: ${total_compra:.2f}")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total a pagar: ${total_final:.2f}")
print("\n¡Gracias por tu compra! ¡Vuelve pronto!")
