import random 
numero_aleatorio = random.randint(1,10)
adivina = int (input("Adivina el numero entre 1 y 10 :"))
print(f"el numero aleatorio es {numero_aleatorio}.")
if adivina == numero_aleatorio:
    print(f"!Correcto! has adivinado el numero.")
else:
    print(f"Incorrecto. el numero era  {numero_aleatorio}. ")