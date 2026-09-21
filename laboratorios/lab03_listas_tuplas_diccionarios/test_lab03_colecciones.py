"""
Pruebas automáticas — Lab 3 refuerzo (Listas, tuplas, dicts, sets)
Corre con: pytest -q
"""
from lab03_colecciones import (
    invertir_lista,
    eliminar_duplicados,
    combinar_en_tupla,
    contar_frecuencias,
    interseccion,
)


def test_invertir_lista():
    original = [1, 2, 3]
    assert invertir_lista(original) == [3, 2, 1]
    assert original == [1, 2, 3]  # no debe modificar la original


def test_eliminar_duplicados_preserva_orden():
    assert eliminar_duplicados([1, 2, 2, 3, 1]) == [1, 2, 3]
    assert eliminar_duplicados([]) == []


def test_combinar_en_tupla():
    assert combinar_en_tupla([1, 2], ["a", "b"]) == [(1, "a"), (2, "b")]


def test_contar_frecuencias():
    assert contar_frecuencias(["a", "b", "a"]) == {"a": 2, "b": 1}
    assert contar_frecuencias([]) == {}


def test_interseccion():
    resultado = interseccion([1, 2, 3], [2, 3, 4])
    assert set(resultado) == {2, 3}
    assert interseccion([1, 2], [3, 4]) == []
