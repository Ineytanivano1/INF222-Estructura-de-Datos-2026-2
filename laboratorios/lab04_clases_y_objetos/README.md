# Lab 4 (refuerzo) — Clases y objetos (POO básica)

**Material de refuerzo de Python · No cuenta para la nota del curso**

---

## Objetivo

Este es **el laboratorio más importante de todo el refuerzo**. Si `lab01_pila.py`
de la semana 1 te resultó confuso por el uso de `class`, `self`, `__init__`,
este lab te lo explica desde cero con ejemplos más simples.

## La idea central

Una clase es un molde para crear objetos. Cada objeto tiene:
- **Atributos**: datos que guarda (ej. `self.nombre`, `self._datos`)
- **Métodos**: funciones que operan sobre esos datos (ej. `es_mayor_de_edad()`, `push()`)

`self` es simplemente "el objeto sobre el que se está llamando el método ahora".
Compara:

```python
# Sin clases (lo que ya sabes hacer)
def es_mayor_de_edad(edad):
    return edad >= 18

es_mayor_de_edad(20)

# Con clases (lo mismo, organizado como objeto)
class Persona:
    def __init__(self, edad):
        self.edad = edad
    def es_mayor_de_edad(self):
        return self.edad >= 18

p = Persona(20)
p.es_mayor_de_edad()   # self = p, automáticamente
```

## Instrucciones

Implementa las clases `Persona` y `Contador` en `lab04_clases.py`.

| Clase | Qué practica |
|-------|---------------|
| `Persona` | `__init__`, atributos, método que lee (`es_mayor_de_edad`), método que modifica (`cumplir_anios`), `__str__` |
| `Contador` | Mismo patrón que usarás en `Pila.size()`: un atributo interno + métodos que lo leen/modifican con reglas (no bajar de 0) |

## Autoevaluación

```bash
pip install pytest   # si no lo hiciste ya
pytest -q
```

## Siguiente paso

Continúa con [`../lab05_recursion_y_errores/`](../lab05_recursion_y_errores/).
Después de este lab, vuelve a `modulo-1-estructuras-lineales/semana-01/laboratorio/lab01_pila.py`
— debería verse mucho más claro.
