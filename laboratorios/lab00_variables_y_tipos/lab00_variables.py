"""
Lab 0 (refuerzo) — Variables, tipos de datos y operadores
INF 222 Estructura de Datos · Material de refuerzo, no cuenta para la nota
Estudiante: _________________________
Fecha: ______________________________

Instrucciones: completa cada función donde dice "# TODO". No cambies el
nombre de la función ni sus parámetros: el test automático depende de ellos.
"""


def resumen_numero(n):
    """
    Recibe un entero o flotante `n` y retorna una tupla con 4 valores:
    (es_par, es_positivo, cuadrado, tipo_como_texto)

    - es_par: True si n es divisible entre 2
    - es_positivo: True si n > 0
    - cuadrado: n elevado al cuadrado
    - tipo_como_texto: el nombre del tipo de `n` como string, ej. "int" o "float"
      (usa la función type() y su atributo __name__)
    """
    # TODO: implementa esta función
    pass


def celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura en Celsius a Fahrenheit.
    Fórmula: F = C * 9/5 + 32
    Retorna un float.
    """
    # TODO: implementa esta función
    pass


def promedio(lista_numeros):
    """
    Recibe una lista de números y retorna el promedio (float).
    Si la lista está vacía, retorna 0.0 (evita división entre cero).
    """
    # TODO: implementa esta función
    pass


def describir_persona(nombre, edad):
    """
    Retorna un string usando f-strings con el formato exacto:
    "<nombre> tiene <edad> años y en 10 años tendrá <edad+10> años."

    Ejemplo: describir_persona("Ana", 20)
    -> "Ana tiene 20 años y en 10 años tendrá 30 años."
    """
    # TODO: implementa esta función
    pass


# =============================================================================
# Zona de pruebas manuales — ejecuta este archivo directamente para ver salidas
# =============================================================================
if __name__ == "__main__":
    print(resumen_numero(4))
    print(resumen_numero(-3.5))
    print(celsius_a_fahrenheit(0))
    print(celsius_a_fahrenheit(100))
    print(promedio([1, 2, 3, 4]))
    print(promedio([]))
    print(describir_persona("Ana", 20))
