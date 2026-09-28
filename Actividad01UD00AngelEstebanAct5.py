# Actividad 05


# PARÁMETROS DESDE LA CONSOLA

import sys


# Con sys.argv podemos recoger los parámetros que ponemos
# al ejecutar el programa desde la consola.

# Por ejemplo:
# python Actividad01UD00AngelEstebanAct5.py Juan 20 Valencia

# sys.argv[0] será el nombre del programa.
# sys.argv[1] será Juan.
# sys.argv[2] será 20.
# sys.argv[3] será Valencia.

print("Nombre del programa:")
print(sys.argv[0])

print("Parámetros introducidos:")
print(sys.argv[1:])


# Podemos acceder a cada parámetro utilizando su posición.

if len(sys.argv) > 1:
    print("Primer parámetro:")
    print(sys.argv[1])

if len(sys.argv) > 2:
    print("Segundo parámetro:")
    print(sys.argv[2])

if len(sys.argv) > 3:
    print("Tercer parámetro:")
    print(sys.argv[3])


# ////////////////////////////////////////////////////////////////////////////////////////

# SOBRECARGA DE FUNCIONES

# En Python podemos hacer que una función reciba un número
# indefinido de parámetros utilizando *.

def mostrar_parametros(*parametros):
    print("Parámetros recibidos:")

    for parametro in parametros:
        print(parametro)


# Podemos pasar diferentes cantidades de parámetros.

mostrar_parametros("Hola")

mostrar_parametros("Hola", "Adiós")

mostrar_parametros("Juan", 20, "Valencia")


# También podemos no pasar ningún parámetro.

mostrar_parametros()
