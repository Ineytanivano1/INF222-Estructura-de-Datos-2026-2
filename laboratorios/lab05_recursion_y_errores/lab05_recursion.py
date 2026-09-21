"""
Lab 5 (refuerzo) — Recursión básica y manejo de errores (try/except/raise)
INF 222 Estructura de Datos · Material de refuerzo, no cuenta para la nota
Estudiante: _________________________
Fecha: ______________________________

Recursión: la vas a usar a fondo en el módulo 3 del curso. Toda función
recursiva necesita dos partes:
  1. CASO BASE: la condición que detiene la recursión (sin esto, recursión
     infinita -> RecursionError).
  2. CASO RECURSIVO: la función se llama a sí misma con un problema más
     pequeño, acercándose al caso base.

Manejo de errores: lo vas a usar en CADA método que pueda fallar, como
pop() o peek() en una pila vacía (revisa lab01_pila.py: "lanza IndexError
si está vacía").
"""


def factorial(n):
    """
    Retorna n! (factorial de n) usando RECURSIÓN (no uses un bucle).
    Caso base: factorial(0) == 1
    Caso recursivo: factorial(n) == n * factorial(n - 1)
    Asume que n >= 0.
    """
    # TODO: implementa esta función de forma recursiva
    pass


def suma_lista_recursiva(lista):
    """
    Retorna la suma de todos los elementos de `lista` usando RECURSIÓN
    (no uses sum() ni un bucle for/while).
    Caso base: lista vacía -> 0
    Caso recursivo: primer elemento + suma_lista_recursiva(resto de la lista)
    Pista: lista[0] es el primer elemento, lista[1:] es "todo menos el primero".
    """
    # TODO: implementa esta función de forma recursiva
    pass


def es_palindromo(texto):
    """
    Retorna True si `texto` se lee igual al derecho y al revés, usando
    RECURSIÓN (no uses slicing texto[::-1] para comparar todo de una vez;
    compara el primer y último carácter y recorre hacia el centro).
    Caso base: texto de longitud 0 o 1 -> True
    Caso recursivo: primer carácter == último carácter Y el texto sin
    esos dos extremos es también un palíndromo.
    Ejemplo: es_palindromo("reconocer") -> True
    """
    # TODO: implementa esta función de forma recursiva
    pass


def dividir_seguro(a, b):
    """
    Retorna a / b.
    Si b es 0, NO dejes que Python lance ZeroDivisionError sin control:
    captúralo con try/except y retorna None en ese caso.
    """
    # TODO: implementa usando try/except
    pass


def obtener_elemento(lista, indice):
    """
    Retorna lista[indice].
    Si `indice` está fuera de rango, captura el IndexError y en su lugar
    lanza (raise) un ValueError con el mensaje exacto:
    f"índice {indice} fuera de rango para una lista de tamaño {len(lista)}"
    """
    # TODO: implementa usando try/except + raise
    pass


if __name__ == "__main__":
    print(factorial(5))
    print(suma_lista_recursiva([1, 2, 3, 4]))
    print(es_palindromo("reconocer"), es_palindromo("python"))
    print(dividir_seguro(10, 2), dividir_seguro(10, 0))
    print(obtener_elemento([1, 2, 3], 1))
