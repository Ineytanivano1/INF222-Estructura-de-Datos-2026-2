"""
Pruebas automáticas — Lab 5 refuerzo (Recursión y errores)
Corre con: pytest -q
"""
import pytest
from lab05_recursion import (
    factorial,
    suma_lista_recursiva,
    es_palindromo,
    dividir_seguro,
    obtener_elemento,
)


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_suma_lista_recursiva():
    assert suma_lista_recursiva([1, 2, 3, 4]) == 10
    assert suma_lista_recursiva([]) == 0
    assert suma_lista_recursiva([7]) == 7


def test_es_palindromo():
    assert es_palindromo("reconocer") is True
    assert es_palindromo("python") is False
    assert es_palindromo("") is True
    assert es_palindromo("a") is True


def test_dividir_seguro_normal():
    assert dividir_seguro(10, 2) == 5


def test_dividir_seguro_por_cero():
    assert dividir_seguro(10, 0) is None


def test_obtener_elemento_valido():
    assert obtener_elemento([1, 2, 3], 1) == 2


def test_obtener_elemento_fuera_de_rango_lanza_valueerror():
    with pytest.raises(ValueError, match="índice 5 fuera de rango para una lista de tamaño 3"):
        obtener_elemento([1, 2, 3], 5)
