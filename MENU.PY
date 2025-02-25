import random
import datetime

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Datos personales")
        print("2. Información estudiantil")
        print("3. Operaciones matemáticas")
        print("4. Verificar paridad")
        print("5. Comparar con diez")
        print("6. Verificar signo")
        print("7. Adivinar número")
        print("8. Calificar nota")
        print("9. Registrar cliente")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            datos_personales()
        elif opcion == "2":
            informacion_estudiantil()
        elif opcion == "3":
            operaciones_matematicas()
        elif opcion == "4":
            verificar_paridad()
        elif opcion == "5":
            comparar_con_diez()
        elif opcion == "6":
            verificar_signo()
        elif opcion == "7":
            adivinar_numero()
        elif opcion == "8":
            calificar_nota()
        elif opcion == "9":
            registrar_cliente()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

def datos_personales():
    nombre = input("¿Cuál es tu nombre? ")
    edad = int(input("¿Cuántos años tienes? "))
    altura = float(input("¿Cuánto mides? (en metros) "))
    print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")

def informacion_estudiantil():
    nombre_completo = input("Ingrese el nombre completo: ")
    carrera = input("Ingrese la carrera: ")
    semestre = int(input("Ingrese el semestre: "))  
    materia = input("Ingrese la materia: ")
    print(f"Nombre: {nombre_completo}\nCarrera: {carrera}\nSemestre: {semestre}\nMateria: {materia}")

def operaciones_matematicas():
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    print(f"\nLa resta de {numero1} - {numero2} es: {numero1 - numero2}")
    print(f"La multiplicación de {numero1} * {numero2} es: {numero1 * numero2}")

def verificar_paridad():
    num = int(input("Ingrese un número: "))
    print(f"{num} es {'par' if num % 2 == 0 else 'impar'}.")

def comparar_con_diez():
    num = int(input("Ingrese un número: "))
    if num > 10:
        print(f"{num} es mayor a 10.")
    else:
        print(f"{num} es menor o igual a 10.")

def verificar_signo():
    num = int(input("Ingrese un número: "))
    if num > 0:
        print(f"{num} es positivo.")
    elif num < 0:
        print(f"{num} es negativo.")
    else:
        print("El número es cero.")

def adivinar_numero():
    numero_aleatorio = random.randint(1, 10)
    adivina = int(input("Adivina el número entre 1 y 10: "))
    print(f"El número aleatorio era {numero_aleatorio}.")
    if adivina == numero_aleatorio:
        print("¡Correcto! Has adivinado el número.")
    else:
        print("Incorrecto.")

def calificar_nota():
    nota = int(input("Ingrese tu calificación (0-100): "))
    if 90 <= nota <= 100:
        print("Tu calificación es: 'A'")
    elif 80 <= nota < 90:
        print("Tu calificación es: 'B'")
    elif 70 <= nota < 80:
        print("Tu calificación es: 'C'")
    elif 60 <= nota < 70:
        print("Tu calificación es: 'D'")
    else:
        print("Tu calificación es: 'F'")

def registrar_cliente():
    nombre = input("Ingrese el nombre: ")
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Nombre del cliente: {nombre}, Fecha y hora: {fecha}")

# Ejecutar el menú
menu()
