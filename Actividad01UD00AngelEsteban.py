import copy
import hashlib

lista1 = [1, 2, ["manzana", "pera"]]
lista2 = copy.copy(lista1) # Creamos las listas y hacemos ShallowCopy.

print("Listas: ")
print(lista1)
print(lista2) # Comprobamos que son iguales.

lista1[2].append("melon") 
""" 

Queremos añadir el melon a la lista de frutas, por lo que
ponemos el [2] que es la posición donde está y usamos .append que añade a la siguiente
posición disponible dentro de la caja. 

"""

print ("Listas con cambios: ")
print("Lista 1 original: ")
print(lista1)
print("Lista 2 copiada: ")
print(lista2)

lista3 = copy.deepcopy(lista1)
lista1[2].append("naranja")

print ("Listas con más cambios: ")
print("Lista 1 original: ")
print(lista1)
print("Lista 3 copiada: ")
print(lista3)

"""

 Como se puede ver aquí, hemos hecho una DeepCopy de la lista 1 y es totalmente
 independiente, es decir que por muchos cambios que le haga ahora a la lista 1 no se
 replicarán en la lista 3

"""

lista4 = ["lechuga","zanahoria", "remolacha", "lechuga"]
print("Lista 4: ")
print(lista4)

lista4.remove("lechuga")
print("Ahora borramos una de las lechugas: ")
print(lista4)

# Para borrar elementos en la lista usaremos .remove y eliminará la primera
# aparición del elemento que elijamos borrar.

print("Ahora vamos a borrar un elemento y guardarlo: ")
print(lista4)
eliminadoL4 = lista4.pop(1)
print("Eliminado: ")
print(eliminadoL4)
print("Lista actual: ")
print(lista4)

# El comando .pop borra un elemento de la lista pero lo guarda en otra variable para
# el uso que le quieras dar.

print ("Para finalizar vamos a borrar un último elemento eligiendo su posición: ")
print(lista4)
del lista4[0]
print ("Lista con elemento borrado: ")
print(lista4)

# Este comando te permite borrar algo eligiendo la posición.

lista5 = [13, 1, 6, 7, 12, 4, 8, 9]
lista6 = lista5[-4:]

print("Nueva lista: ")
print(lista5)
print("Lista con los últimos 4 números: ")
print(lista6) # ShallowCopy

# Al poner lista6 = lista5[-4:] usa la técnica de 'slicing'. Esta técnica, cuando
# le pones el índice negativo le estás pidiendo que cuente desde atrás y con los dos
# puntos que pille los 4.  

cadena = "me gustan las albondigas"
listaCadena = cadena.split()

print("Oración: ")
print(cadena)
print("Oración convertida a lista: ")
print(listaCadena)

# El comando .split te permite convertir las palabras de una cadena en una lista 
# SIEMPRE Y CUANDO estén separadas por espacios.

# ////////////////////////////////////////////////////////////////////////////////////////

# Actividad 02


# Función que recibe dos números y los suma

def suma(a, b):
    return a + b

numSuma1 = int(input("Dame un número para sumar: "))
numSuma2 = int(input("Dame otro número para sumar: "))

resultado = suma(numSuma1, numSuma2)
print("La suma ha dado: ")
print(resultado)

# Para definir una función ponemos 'def', el nombre de la función y las variables
# que recibe. Tras eso dentro de la función puedes hacer lo que quieras y con return
# devolver lo que quieras, tampoco tienes porqué devolver nada.

listaFuncion = [10, 20, 30, 40, 50]

def doblar_lista(listaFuncion):
    for i in range(len(listaFuncion)):
        listaFuncion[i] = listaFuncion[i] * 2

print("Lista antes de doblar")
print(listaFuncion)

doblar_lista(listaFuncion)

print("Lista doblada")
print(listaFuncion)

# La función coge una lista en el () y con ella hace lo que quiera, en este caso
# usa el for each para que cada elemento sea multiplicado por 2

listaFuncionCopia = [0]

def copia_doblant(lista):
    copia = lista.copy()

    for i in range(len(copia)):
        copia[i] = copia[i] * 2

    return copia

listaFuncionCopia = copia_doblant(listaFuncion)

print("Lista original")
print(listaFuncion)
print("Lista copiada y doblada")
print(listaFuncionCopia)

# Esta función coge una lista, la copia y luego hace lo mismo que la anterior, esta
# vez te devuelve (return) la copia para que la guardes, en vez de modificar la
# original permanentemente

# ////////////////////////////////////////////////////////////////////////////////////////

# Actividad 03


# Vamos a guardar usuarios y contraseñas utilizando una lista.
# Las contraseñas se guardarán en formato Hash mediante SHA-256.


# Función que convierte una contraseña a Hash
def hacer_hash(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()


# Lista con 5 usuarios y sus contraseñas en Hash
usuariosLista = [
    ["juan", hacer_hash("1234")],
    ["maria", hacer_hash("abcd")],
    ["pedro", hacer_hash("python")],
    ["laura", hacer_hash("clave123")],
    ["ana", hacer_hash("hola")]
]

print("Lista de usuarios y contraseñas:")
print(usuariosLista)


# Función para consultar un usuario en la lista
def consultar_lista(usuario, contraseña):
    contraseñaHash = hacer_hash(contraseña)

    for usuarioLista in usuariosLista:
        if usuarioLista[0] == usuario and usuarioLista[1] == contraseñaHash:
            return True

    return False


# Hacemos dos consultas
print("Consulta 1:")
print(consultar_lista("juan", "1234"))

print("Consulta 2:")
print(consultar_lista("juan", "contraseñaIncorrecta"))


# -------------------------------------------------------------------

# Ahora hacemos lo mismo utilizando un diccionario.
# En este caso el usuario será la clave y el Hash de la contraseña será el valor.

usuariosDiccionario = {
    "juan": hacer_hash("1234"),
    "maria": hacer_hash("abcd"),
    "pedro": hacer_hash("python"),
    "laura": hacer_hash("clave123"),
    "ana": hacer_hash("hola")
}

print("Diccionario de usuarios y contraseñas:")
print(usuariosDiccionario)


# Función para consultar un usuario en el diccionario
def consultar_diccionario(usuario, contraseña):
    contraseñaHash = hacer_hash(contraseña)

    if usuario in usuariosDiccionario:
        if usuariosDiccionario[usuario] == contraseñaHash:
            return True

    return False


# Hacemos dos consultas
print("Consulta 1:")
print(consultar_diccionario("maria", "abcd"))

print("Consulta 2:")
print(consultar_diccionario("maria", "contraseñaIncorrecta"))

# ////////////////////////////////////////////////////////////////////////////////////////

# Actividad 04


# OPERADOR "is"
# El operador "is" comprueba si dos variables hacen referencia al mismo objeto.
# No comprueba simplemente si tienen el mismo contenido.

listaIs1 = [1, 2, 3]
listaIs2 = listaIs1
listaIs3 = [1, 2, 3]

print("¿listaIs1 y listaIs2 son el mismo objeto?")
print(listaIs1 is listaIs2)

print("¿listaIs1 y listaIs3 son el mismo objeto?")
print(listaIs1 is listaIs3)


# Como listaIs2 apunta a la misma lista que listaIs1, devuelve True.
# Aunque listaIs3 tenga exactamente los mismos elementos, es otra lista
# diferente, por lo que devuelve False.


# OPERADOR "not"
# El operador "not" sirve para negar una condición.
# Si algo es True, "not" lo convierte en False.
# Si algo es False, "not" lo convierte en True.

numero = 10

print("¿El número NO es igual a 10?")
print(not numero == 10)

print("¿El número NO es igual a 5?")
print(not numero == 5)


# OPERADOR "in"
# El operador "in" sirve para comprobar si un elemento está dentro
# de una lista, cadena de texto, diccionario, etc.

frutas = ["manzana", "pera", "plátano"]

print("¿La manzana está en la lista?")
print("manzana" in frutas)

print("¿La naranja está en la lista?")
print("naranja" in frutas)


# También podemos utilizar "not in" para comprobar que un elemento
# NO está dentro de una lista.

print("¿La naranja NO está en la lista?")
print("naranja" not in frutas)

# ////////////////////////////////////////////////////////////////////////////////////////

# Actividad 06


# Creamos una lista en la que cada elemento tiene dos valores:
# el primero será la altura y el segundo será el peso.

personas = [
    [175, 70],
    [180, 80],
    [165, 60],
    [180, 75],
    [170, 65],
    [175, 68]
]

print("Lista original:")
print(personas)


# Para ordenar la lista utilizamos sorted().
# Queremos que la altura vaya de mayor a menor y que,
# en caso de tener la misma altura, el peso vaya de menor a mayor.

def ordenar_persona(persona):
    return (-persona[0], persona[1])


personasOrdenadas = sorted(personas, key=ordenar_persona)

print("Lista ordenada:")
print(personasOrdenadas)


# Una key function es una función que recibe un elemento de la lista
# y devuelve el valor que queremos utilizar para ordenar ese elemento.

# En este caso recibe una persona, que es una lista con altura y peso.
# Devuelve (-altura, peso).

# Ponemos la altura en negativo para conseguir que se ordene
# de mayor a menor.

# El peso lo dejamos positivo para que, en caso de empate de altura,
# se ordene de menor a mayor.

# La función key se ejecuta una vez para cada elemento de la lista
# y Python utiliza los valores que devuelve para realizar la ordenación.



