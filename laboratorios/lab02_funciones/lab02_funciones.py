"""Lab 2 (refuerzo) — Funciones: parámetros, retorno, valores por defecto, *args
INF 222 Estructura de Datos · Material de refuerzo, no cuenta para la nota
Estudiante: _________________________
Fecha: ______________________________"""


def es_primo(n):
    """Retorna True si `n` es un número primo, False en caso contrario.
    Considera que n < 2 nunca es primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def potencia(base, exponente=2):
    """Retorna base elevado a exponente. Si no se pasa exponente, usa 2
    (o sea, calcula el cuadrado por defecto).
    No uses el operador **, calcúlalo con un bucle (es para practicar)."""
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado  # <-- El return debe ir FUERA del bucle for


def sumar_todos(*numeros):
    """
    Recibe una cantidad variable de números (*args) y retorna la suma
    de todos. sumar_todos() sin argumentos retorna 0.
    Ejemplo: sumar_todos(1, 2, 3) -> 6"""
    return sum(numeros)


def crear_mensaje(nombre, saludo="Hola"):
    """Retorna un string "<saludo>, <nombre>!" usando un parámetro con valor
    por defecto para `saludo`.
    Ejemplo: crear_mensaje("Ana") -> "Hola, Ana!"
    Ejemplo: crear_mensaje("Ana", "Buenos días") -> "Buenos días, Ana!"""
    return f"{saludo}, {nombre}!"


def aplicar_operacion(lista_numeros, operacion):
    """Recibe una lista de números y una FUNCIÓN `operacion` (una función es
    un valor como cualquier otro en Python, y se puede pasar como
    parámetro). Retorna una nueva lista con `operacion` aplicada a cada
    elemento.
    Ejemplo: aplicar_operacion([1, 2, 3], lambda x: x * 2) -> [2, 4, 6]"""
    return [operacion(x) for x in lista_numeros]


if __name__ == "__main__":
    print(es_primo(7), es_primo(8), es_primo(1))
    print(potencia(3), potencia(2, 5))
    print(sumar_todos(1, 2, 3), sumar_todos())
    print(crear_mensaje("Ana"), crear_mensaje("Ana", "Buenos días"))
    print(aplicar_operacion([1, 2, 3], lambda x: x * 2))