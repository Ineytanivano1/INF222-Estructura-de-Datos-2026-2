class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class PilaEnlazada:
    def __init__(self):
        self._cabeza = None
        self._tamano = 0

    def push(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self._cabeza
        self._cabeza = nuevo_nodo
        self._tamano += 1

    def is_empty(self):
        return self._cabeza is None

    def size(self):
        return self._tamano

    def pop(self):
        if self.is_empty():
            raise IndexError("pop es una pila vacia")
        dato = self._cabeza.dato
        self._cabeza = self._cabeza.siguiente
        self._tamano -= 1
        return dato

    def peek(self):
        if self.is_empty():
            raise IndexError("peek de una pila vacia")
        return self._cabeza.dato

    def __str__(self):
        elementos = []
        actual = self._cabeza
        while actual is not None:
         elementos.append(str(actual.dato))
         actual = actual.siguiente
        return "cabeza -> [" + " ->".join(elementos) + "]"
