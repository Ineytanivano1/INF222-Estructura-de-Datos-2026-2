"""
Lab 1 (refuerzo) — Control de flujo: if/elif/else, while, for
INF 222 Estructura de Datos · Material de refuerzo, no cuenta para la nota
Estudiante: _________________________
Fecha: ______________________________
"""


def clasificar_edad(edad):
    """
    Retorna un string según la edad:
      - "niño"     si edad < 13
      - "adolescente" si 13 <= edad < 18
      - "adulto"   si edad >= 18
    """
    # TODO: implementa con if/elif/else
    pass


def contar_hasta(n):
    """
    Retorna una lista con los números del 1 al n (incluido), usando un
    bucle `while` (no uses range() aquí, es para practicar while).
    Si n <= 0, retorna una lista vacía.
    """
    # TODO: implementa con while
    pass


def suma_pares(n):
    """
    Retorna la suma de todos los números pares entre 1 y n (incluido),
    usando un bucle `for` con `range()`.
    Ejemplo: suma_pares(10) -> 2+4+6+8+10 = 30
    """
    # TODO: implementa con for + range
    pass


def primer_multiplo(numero, limite):
    """
    Busca, entre 1 y `limite` (incluido), el primer valor que sea múltiplo
    de `numero`. Usa `break` para detener el bucle apenas lo encuentres.
    Si no existe ninguno, retorna None.
    Ejemplo: primer_multiplo(7, 30) -> 7
    """
    # TODO: implementa con for + break
    pass


def solo_positivos(lista_numeros):
    """
    Retorna una nueva lista que contiene solo los números positivos de
    `lista_numeros` (> 0), preservando el orden. Usa `continue` para saltar
    los que no cumplen la condición (no uses list comprehension aquí).
    """
    # TODO: implementa con for + continue
    pass


if __name__ == "__main__":
    print(clasificar_edad(10), clasificar_edad(15), clasificar_edad(30))
    print(contar_hasta(5))
    print(suma_pares(10))
    print(primer_multiplo(7, 30))
    print(solo_positivos([-2, 5, 0, -1, 8, 3]))
