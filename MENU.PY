import math
import random
import datetime

def menu():
    while True:
        print("\n********** MENÚ DE EJERCICIOS ********")
        print("1. Información del estudiante")
        print("2. Datos personales")
        print("3. Suma de dos números")
        print("4. Resta y multiplicación")
        print("5. Área de un círculo")
        print("6. Número par o impar")
        print("7. Comparación con 10")
        print("8. Positivo, negativo o cero")
        print("9. Adivinar número")
        print("10. Calificación en letras")
        print("11. Fecha y hora con nombre")
        print("12. Descuento en compra")
        print("13. Generar ticket de compra")
        print("14. Lista de valores")
        print("15. Lista enlazada básica")
        print("16. Agente de decisión")
        print("17. Movimiento de agentes")
        print("18. Búsqueda en grafos (DFS)")
        print("19. Heurística de valores")
        print("20. Salir")
        
        opcion = input("Seleccione un ejercicio del 1 al 20: ")
        
        if opcion == "1":
            nombre_completo = input("Ingrese el nombre completo: ")
            carrera = input("Ingrese la carrera: ")
            semestre = int(input("Ingrese el semestre: "))
            materia = input("Ingrese la materia: ")
            print(f"Nombre: {nombre_completo}\nCarrera: {carrera}\nSemestre: {semestre}\nMateria: {materia}")
        
        elif opcion == "2":
            nombre = input("¿Cuál es tu nombre? ")
            edad = int(input("¿Cuántos años tienes? "))
            altura = float(input("¿Cuánto mides? (en metros) "))
            print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")
        
        elif opcion == "3":
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            print(f"La suma de {num1} y {num2} es: {num1 + num2}")
        
        elif opcion == "4":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(f"La resta es: {num1 - num2}\nLa multiplicación es: {num1 * num2}")
        
        elif opcion == "5":
            radio = float(input("Introduzca el radio de un círculo: "))
            area = math.pi * (radio ** 2)
            print(f"El área del círculo es: {area:.2f} metros cuadrados")
        
        elif opcion == "6":
            num = int(input("Ingrese un número: "))
            print(f"{num} es {'par' if num % 2 == 0 else 'impar'}.")
        
        elif opcion == "7":
            num = int(input("Ingrese un número: "))
            print(f"{num} es {'mayor' if num > 10 else 'menor o igual'} a 10.")
        
        elif opcion == "8":
            num = int(input("Ingrese un número: "))
            if num > 0:
                print("El número es positivo.")
            elif num < 0:
                print("El número es negativo.")
            else:
                print("El número es cero.")
        
        elif opcion == "9":
            numero_aleatorio = random.randint(1, 10)
            adivina = int(input("Adivina el número entre 1 y 10: "))
            print(f"El número aleatorio es {numero_aleatorio}.")
            if adivina == numero_aleatorio:
                print("¡Correcto! Has adivinado el número.")
            else:
                print(f"Incorrecto. El número era {numero_aleatorio}.")
        
        elif opcion == "10":
            nota = int(input("Ingrese tu calificación (0-100): "))
            if nota >= 90:
                print("Tu calificación es A")
            elif nota >= 80:
                print("Tu calificación es B")
            elif nota >= 70:
                print("Tu calificación es C")
            elif nota >= 60:
                print("Tu calificación es D")
            else:
                print("Tu calificación es F")
        
        elif opcion == "11":
            nombre = input("Ingrese el nombre: ")
            fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Nombre del cliente: {nombre}\nFecha y hora: {fecha}")
        
        elif opcion == "12":
            total = float(input("Ingrese el total de la compra: "))
            descuento = total * 0.10 if total > 100 else 0
            print(f"Total a pagar: {total - descuento:.2f}")
        
        elif opcion == "13":
            nombre_tienda = "Tienda OXXO"
            folio = random.randint(1000, 9999)
            fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            nombre = input("Ingresa tu nombre: ")
            producto = input("Ingresa el nombre del producto: ")
            precio = float(input("Ingresa el precio unitario del producto: "))
            cantidad = int(input("Ingresa la cantidad: "))
            total_compra = precio * cantidad
            descuento = total_compra * 0.10 if total_compra > 100 else 0
            total_final = total_compra - descuento
            print("\n===== TICKET DE COMPRA =====")
            print(f"Tienda: {nombre_tienda}")
            print(f"Folio: {folio}")
            print(f"Fecha y hora: {fecha_hora}")
            print(f"Cliente: {nombre}")
            print(f"Producto: {producto}")
            print(f"Total de la compra: ${total_compra:.2f}")
            print(f"Descuento aplicado: ${descuento:.2f}")
            print(f"Total a pagar: ${total_final:.2f}")
            print("\n¡Gracias por tu compra!")

        elif opcion == "14":
            valores = [input(f"Ingrese el valor {i+1}: ") for i in range(4)]
            print("Valores ingresados:", valores)

        elif opcion == "15":
            class Nodo:
                def __init__(self, valor):
                    self.valor = valor
                    self.siguiente = None
            nodo1 = Nodo(input("Ingrese el valor del primer nodo: "))
            nodo2 = Nodo(input("Ingrese el valor del segundo nodo: "))
            nodo1.siguiente = nodo2
            print(f"Lista enlazada: {nodo1.valor} -> {nodo2.valor}")

        elif opcion == "16":
            opciones = ["ir al cine", "estudiar", "hacer ejercicio"]
            prioridades = ["hacer ejercicio", "estudiar"]
            print(f"El agente decide: {opciones[0]}" if opciones[0] in prioridades else "No decide nada")

        elif opcion == "17":
            class Agente:
                def __init__(self, nombre, ubicacion):
                    self.nombre = nombre
                    self.ubicacion = ubicacion
                def mover(self, nueva_ubicacion):
                    self.ubicacion = nueva_ubicacion
                    print(f"{self.nombre} se movió a {self.ubicacion}")
            agente1 = Agente("Agente 1", "A")
            agente2 = Agente("Agente 2", "B")
            agente1.mover("C")
            agente2.mover("C")
            print("Los agentes se han encontrado" if agente1.ubicacion == agente2.ubicacion else "Los agentes no se han encontrado")

        elif opcion == "18":
            grafos = {
                'A': ['B', 'C'],
                'B': ['D', 'E'],
                'C': ['F'],
                'D': [],
                'E': ['F'],
                'F': [],
            } 

            def dfs(grafo, nodo, visitados=None):
                if visitados is None:
                    visitados = set()
                visitados.add(nodo)
                for vecino in grafo[nodo]:
                    if vecino not in visitados:
                        dfs(grafo, vecino, visitados)
                return visitados

            resultado = dfs(grafos, 'A')
            print(f"Nodos visitados por DFS: {resultado}")

        elif opcion == "19":
            valores = [20, 35, 55, 60, 70]
            objetivo = 50
            mejor_valor = min(valores, key=lambda x: abs(x - objetivo))
            print(f"El valor más cercano a {objetivo} es: {mejor_valor}")

        elif opcion == "20":
            print("Saliendo del programa...")
            break

menu()
