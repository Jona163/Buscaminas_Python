# Autor: Jonathan Hernández
# Fecha: 13 octubre 2024
# Descripción: Buscaminas en Python.
# GitHub: https://github.com/Jona163

from random import randint

# Juego de Buscaminas desarrollado en Python.
# Crear matriz, esta función no invoca ninguna otra función del programa.
def matriz(filas, columnas, caracter=False):
    tablero = []
    for i in range(filas):
        v = [caracter] * columnas
        tablero.append(v)
    return tablero

# Poner minas aleatoriamente, esta función no invoca ninguna otra función del programa.
def minas(filas, columnas, tablero, minaz):
    mi = 1
    while mi <= minaz:
        fil = randint(0, filas - 1)
        col = randint(0, columnas - 1)
        if not tablero[fil][col]:
            tablero[fil][col] = True
            mi += 1
    return tablero

# Crear el tablero de acuerdo a las especificaciones del jugador.
def tablero1():
    opcion = int(input("Quiere un juego aleatorio (si = 1)(no = 0): "))
    if opcion:
        while True:
            print("¿Qué dificultad desea?")
            print("\t1. Fácil.")
            print("\t2. Medio.")
            print("\t3. Difícil.")
            opcion = input("Elija una opción (f o fácil)(m o medio)(d o difícil): ").lower()
            if opcion in ("f", "fácil"):
                tablero = matriz(15, 10)
                minas(15, 10, tablero, 75)
               return tablero, 15, 10
            elif opcion in ("m", "medio"):
                tablero = matriz(25, 20)
                minas(25, 20, tablero, 250)
                return tablero, 25, 20
            elif opcion in ("d", "difícil"):
                tablero = matriz(35, 30)
                minas(35, 30, tablero, 525)
                return tablero, 35, 30
            else:
                print("Debe escoger una de las opciones del menú.")
   else:
        filas = int(input("Ingresa el número de filas que deseas: "))
        columnas = int(input("Ingresa el número de columnas que desea: "))
        while True:
            mina = int(input("Ingresa el número de minas que desea: "))
            if mina <= filas * columnas:
                break
            print(f"El número de minas debe ser menor que {filas * columnas}.")
        tablero = matriz(filas, columnas)
        minas(filas, columnas, tablero, mina)
        return tablero, filas, columnas

# Poner las pistas, que son los números que aparecen en el tablero.
def numeros(tablero, filas, columnas):
    nueva = matriz(filas, columnas, ".")
    for i in range(filas):
        for j in range(columnas):
            # Calcular el número de vecinos de la celda actual.
            n = 0
            if i > 0 and j > 0 and tablero[i - 1][j - 1]:
                n += 1
            if j > 0 and tablero[i][j - 1]:
                n += 1
            if i < filas - 1 and j > 0 and tablero[i + 1][j - 1]:
                n += 1
            if i > 0 and tablero[i - 1][j]:
                n += 1
            if i < filas - 1 and tablero[i + 1][j]:
                n += 1
            if i > 0 and j < columnas - 1 and tablero[i - 1][j + 1]:
                n += 1
            if j < columnas - 1 and tablero[i][j + 1]:
                n += 1
            if i < filas - 1 and j < columnas - 1 and tablero[i + 1][j + 1]:
                n += 1
            if not tablero[i][j]:
                nueva[i][j] = n
            else:
                nueva[i][j] = "*"
    return nueva

# Mostrar el tablero de juego.
def mostrar(tablero, filas, columnas, caracter):
    for i in range(filas):
        for j in range(columnas):
            if j != columnas - 1:
                if isinstance(tablero[i][j], (int, str)):
                    print(tablero[i][j], end=" ")
                elif isinstance(tablero[i][j], bool) and tablero[i][j]:
                    print("*", end=" ")
                else:
                    print(caracter, end=" ")
            else:
                if isinstance(tablero[i][j], (int, str)):
                    print(tablero[i][j])
                elif isinstance(tablero[i][j], bool) and tablero[i][j]:
                    print("*")
                else:
                    print(caracter)
