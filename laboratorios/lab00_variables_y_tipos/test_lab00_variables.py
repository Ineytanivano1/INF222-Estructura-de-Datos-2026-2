"""
Pruebas automáticas — Lab 0 refuerzo (Variables y tipos)
Corre con: pytest -q  (parado dentro de esta carpeta, o desde la raíz del repo)
"""
from lab00_variables import (
    resumen_numero,
    celsius_a_fahrenheit,
    promedio,
    describir_persona,
)


def test_resumen_numero_par_positivo():
    assert resumen_numero(4) == (True, True, 16, "int")


def test_resumen_numero_impar_negativo_float():
    es_par, es_positivo, cuadrado, tipo = resumen_numero(-3.5)
    assert es_par is False
    assert es_positivo is False
    assert cuadrado == 12.25
    assert tipo == "float"


def test_celsius_a_fahrenheit():
    assert celsius_a_fahrenheit(0) == 32
    assert celsius_a_fahrenheit(100) == 212


def test_promedio_lista_normal():
    assert promedio([1, 2, 3, 4]) == 2.5


def test_promedio_lista_vacia_no_falla():
    assert promedio([]) == 0.0


def test_describir_persona():
    assert describir_persona("Ana", 20) == "Ana tiene 20 años y en 10 años tendrá 30 años."
