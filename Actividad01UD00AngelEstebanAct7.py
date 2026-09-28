# Actividad 07


import random


# Creamos la clase Car.
# Cada coche tendrá una matrícula y un color.

class Car:

    # Este método se utiliza para crear cada coche.
    def __init__(self, matricula, color):
        self.matricula = matricula
        self.color = color


    # Método para imprimir los datos del coche.
    def imprimir(self):
        print("Matrícula:", self.matricula)
        print("Color:", self.color)


    # Primer método que hemos añadido.
    def arrancar(self):
        print("El coche con matrícula", self.matricula, "ha arrancado.")


    # Segundo método que hemos añadido.
    def parar(self):
        print("El coche con matrícula", self.matricula, "se ha parado.")


# Pedimos al usuario cuántos coches quiere crear.

n = int(input("¿Cuántos coches quieres crear? "))


# Creamos la lista de colores que podremos utilizar.

colores = ["red", "white", "black", "pink", "blue"]


# Creamos una lista donde guardaremos todos los coches.

coches = []


# Creamos tantos coches como haya indicado el usuario.
# La matrícula será un número consecutivo empezando desde 1.
# El color se elegirá aleatoriamente de la lista de colores.

for i in range(1, n + 1):

    color = random.choice(colores)

    coche = Car(i, color)

    coches.append(coche)


# Finalmente imprimimos las primeras 10 instancias.
# Si n es menor que 10, solamente imprimiremos las que existan.

cantidad = min(n, 10)


for i in range(cantidad):

    print("Coche", i + 1)

    coches[i].imprimir()

    print()

for coche in coches:

    coche.arrancar()
    coche.parar()