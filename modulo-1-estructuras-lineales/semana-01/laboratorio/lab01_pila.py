class Pila:
    def __init__(self):
        self.datos = []
    def pop(self):
     if self.is_empty():
        raise IndexError("pop en pila vacía")
     return self.datos.pop()
    def is_empty(self):
        return len(self.datos) ==0       
pila = Pila()
# quien usa la pila:
try:
    pila.pop()
except IndexError:
    print("La pila estaba vacia")