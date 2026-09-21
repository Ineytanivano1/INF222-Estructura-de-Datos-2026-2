"""
Lab 3 (refuerzo) — Listas, tuplas, diccionarios y sets
INF 222 Estructura de Datos · Material de refuerzo, no cuenta para la nota
Estudiante: _________________________
Fecha: ______________________________

Estas son las estructuras de datos QUE YA TRAE PYTHON. Este curso te enseña
a construir tus propias versiones (Pila, ListaEnlazada, Árbol...), pero
primero necesitas dominar las que ya existen: se usan como "contenedor
interno" en varios laboratorios (revisa lab01_pila.py de semana 1).
"""


def invertir_lista(lista):
    """
    Retorna una NUEVA lista con los elementos en orden inverso.
    No modifiques la lista original (no uses .reverse()).
    Ejemplo: invertir_lista([1, 2, 3]) -> [3, 2, 1]
    """
    # TODO: implementa esta función (pista: slicing lista[::-1] o un for)
    pass


def eliminar_duplicados(lista):
    """
    Retorna una nueva lista sin elementos duplicados, preservando el
    ORDEN de la primera aparición de cada elemento.
    Ejemplo: eliminar_duplicados([1, 2, 2, 3, 1]) -> [1, 2, 3]
    (No uses set() directamente para el resultado final porque los sets
    no garantizan orden; puedes usar un set auxiliar para verificar si
    ya viste un elemento).
    """
    # TODO: implementa esta función
    pass


def combinar_en_tupla(lista_a, lista_b):
    """
    Recibe dos listas de igual longitud y retorna una lista de TUPLAS,
    donde cada tupla es (elemento_de_a, elemento_de_b) en la misma posición.
    Ejemplo: combinar_en_tupla([1, 2], ["a", "b"]) -> [(1, "a"), (2, "b")]
    Pista: la función zip() hace exactamente esto.
    """
    # TODO: implementa esta función
    pass


def contar_frecuencias(palabras):
    """
    Recibe una lista de strings y retorna un diccionario donde cada clave
    es una palabra y el valor es cuántas veces aparece.
    Ejemplo: contar_frecuencias(["a", "b", "a"]) -> {"a": 2, "b": 1}
    """
    # TODO: implementa esta función (pista: diccionario.get(clave, 0))
    pass


def interseccion(lista_a, lista_b):
    """
    Retorna una lista (sin duplicados, en cualquier orden) con los
    elementos que aparecen en AMBAS listas. Usa sets y el operador `&`.
    Ejemplo: interseccion([1, 2, 3], [2, 3, 4]) -> lista con 2 y 3
    """
    # TODO: implementa esta función
    pass


if __name__ == "__main__":
    print(invertir_lista([1, 2, 3]))
    print(eliminar_duplicados([1, 2, 2, 3, 1]))
    print(combinar_en_tupla([1, 2], ["a", "b"]))
    print(contar_frecuencias(["a", "b", "a"]))
    print(interseccion([1, 2, 3], [2, 3, 4]))
