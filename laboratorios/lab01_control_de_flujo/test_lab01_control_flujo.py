"""
Pruebas automáticas — Lab 1 refuerzo (Control de flujo)
Corre con: pytest -q
"""
from lab01_control_flujo import (
    clasificar_edad,
    contar_hasta,
    suma_pares,
    primer_multiplo,
    solo_positivos,
)


def test_clasificar_edad():
    assert clasificar_edad(10) == "niño"
    assert clasificar_edad(15) == "adolescente"
    assert clasificar_edad(30) == "adulto"
    assert clasificar_edad(18) == "adulto"
    assert clasificar_edad(13) == "adolescente"


def test_contar_hasta():
    assert contar_hasta(5) == [1, 2, 3, 4, 5]
    assert contar_hasta(0) == []
    assert contar_hasta(-3) == []


def test_suma_pares():
    assert suma_pares(10) == 30
    assert suma_pares(1) == 0


def test_primer_multiplo_existe():
    assert primer_multiplo(7, 30) == 7
    assert primer_multiplo(9, 30) == 9


def test_primer_multiplo_no_existe():
    assert primer_multiplo(50, 10) is None


def test_solo_positivos():
    assert solo_positivos([-2, 5, 0, -1, 8, 3]) == [5, 8, 3]
    assert solo_positivos([-1, -2]) == []
