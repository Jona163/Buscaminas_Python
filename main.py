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
