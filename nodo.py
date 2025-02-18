class Nodo:
    def __init__(self, valor):#contructor 
        self.valor = valor#asigna
        self.siguiente = None

nodo1 = Nodo(input("Ingrese el valor del primer nodo: "))
nodo2 = Nodo(input("Ingrese el valor del segundo nodo: "))
nodo1.siguiente = nodo2
3

print("Valores de la lista enlazada:")
print(nodo1.valor, "->", nodo1.siguiente.valor)
