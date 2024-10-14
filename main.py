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
