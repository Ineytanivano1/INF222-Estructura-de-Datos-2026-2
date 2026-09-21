"""
Pruebas automáticas — Lab 2 refuerzo (Funciones)
Corre con: pytest -q
"""
from lab02_funciones import (
    es_primo,
    potencia,
    sumar_todos,
    crear_mensaje,
    aplicar_operacion,
)


def test_es_primo():
    assert es_primo(7) is True
    assert es_primo(8) is False
    assert es_primo(1) is False
    assert es_primo(2) is True


def test_potencia_valor_por_defecto():
    assert potencia(3) == 9


def test_potencia_con_exponente():
    assert potencia(2, 5) == 32


def test_sumar_todos_con_valores():
    assert sumar_todos(1, 2, 3) == 6


def test_sumar_todos_sin_valores():
    assert sumar_todos() == 0


def test_crear_mensaje_por_defecto():
    assert crear_mensaje("Ana") == "Hola, Ana!"


def test_crear_mensaje_personalizado():
    assert crear_mensaje("Ana", "Buenos días") == "Buenos días, Ana!"


def test_aplicar_operacion():
    assert aplicar_operacion([1, 2, 3], lambda x: x * 2) == [2, 4, 6]
    assert aplicar_operacion([1, 2, 3], lambda x: x + 1) == [2, 3, 4]
