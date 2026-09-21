"""
Pruebas automáticas — Lab 4 refuerzo (Clases y objetos)
Corre con: pytest -q
"""
from lab04_clases import Persona, Contador


def test_persona_constructor_y_str():
    p = Persona("Ana", 20)
    assert str(p) == "Ana (20 años)"


def test_persona_es_mayor_de_edad():
    assert Persona("Ana", 20).es_mayor_de_edad() is True
    assert Persona("Luis", 15).es_mayor_de_edad() is False
    assert Persona("Bob", 18).es_mayor_de_edad() is True


def test_persona_cumplir_anios():
    p = Persona("Ana", 17)
    p.cumplir_anios()
    assert p.edad == 18
    assert p.es_mayor_de_edad() is True


def test_contador_empieza_en_cero():
    c = Contador()
    assert c.valor() == 0


def test_contador_incrementar():
    c = Contador()
    c.incrementar()
    c.incrementar(5)
    assert c.valor() == 6


def test_contador_decrementar_no_baja_de_cero():
    c = Contador()
    c.incrementar(3)
    c.decrementar(100)
    assert c.valor() == 0


def test_contador_reiniciar():
    c = Contador()
    c.incrementar(10)
    c.reiniciar()
    assert c.valor() == 0
