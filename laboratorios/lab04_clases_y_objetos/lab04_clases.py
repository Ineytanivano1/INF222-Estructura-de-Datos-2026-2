"""
Lab 4 (refuerzo) — Clases y objetos (POO básica)
INF 222 Estructura de Datos · Material de refuerzo, no cuenta para la nota
Estudiante: _________________________
Fecha: ______________________________

Esta es la habilidad más importante para el resto del curso: TODA estructura
de datos que vas a construir (Pila, Cola, Nodo, ListaEnlazada, Árbol...) es
una clase de Python. Si dominas este laboratorio, lab01_pila.py de la
semana 1 te va a resultar familiar.
"""


class Persona:
    """Representa a una persona con nombre y edad."""

    def __init__(self, nombre, edad):
        """
        Guarda `nombre` y `edad` como atributos de instancia.
        Usa self.nombre = ... y self.edad = ...
        """
        # TODO: implementa el constructor
        pass

    def es_mayor_de_edad(self):
        """Retorna True si self.edad >= 18."""
        # TODO: implementa este método
        pass

    def cumplir_anios(self):
        """Incrementa self.edad en 1. No retorna nada (modifica el objeto)."""
        # TODO: implementa este método
        pass

    def __str__(self):
        """
        Retorna un string con el formato exacto:
        "<nombre> (<edad> años)"
        Ejemplo: "Ana (20 años)"
        """
        # TODO: implementa este método
        pass


class Contador:
    """
    Un contador simple que empieza en 0 y se puede incrementar,
    decrementar y reiniciar. Modela el mismo patrón que vas a usar en
    Pila.size(): un atributo interno que los métodos leen y modifican.
    """

    def __init__(self):
        """Inicializa el contador en 0."""
        # TODO: implementa el constructor
        pass

    def incrementar(self, cantidad=1):
        """Suma `cantidad` (por defecto 1) al contador."""
        # TODO: implementa este método
        pass

    def decrementar(self, cantidad=1):
        """
        Resta `cantidad` (por defecto 1) al contador.
        El contador nunca debe bajar de 0 (si se pasaría de 0, queda en 0).
        """
        # TODO: implementa este método
        pass

    def reiniciar(self):
        """Vuelve el contador a 0."""
        # TODO: implementa este método
        pass

    def valor(self):
        """Retorna el valor actual del contador."""
        # TODO: implementa este método
        pass


if __name__ == "__main__":
    p = Persona("Ana", 17)
    print(p)
    print(p.es_mayor_de_edad())
    p.cumplir_anios()
    print(p, p.es_mayor_de_edad())

    c = Contador()
    c.incrementar()
    c.incrementar(5)
    print(c.valor())
    c.decrementar(100)
    print(c.valor())
