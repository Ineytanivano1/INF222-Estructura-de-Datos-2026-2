# Lab 5 (refuerzo) — Recursión básica y manejo de errores

**Material de refuerzo de Python · No cuenta para la nota del curso**

---

## Objetivo

Recursión (base directa del módulo 3 del curso: "Recursividad, Ordenación y
Búsqueda") y manejo de errores con `try/except/raise` (lo vas a necesitar en
`pop()`/`peek()` de `Pila`, y en cada estructura enlazada de aquí en adelante).

## La plantilla mental para recursión

Toda función recursiva sigue el mismo esqueleto:

```python
def funcion_recursiva(problema):
    if es_caso_base(problema):          # 1. CASO BASE — detiene la recursión
        return valor_directo

    return combinar(                     # 2. CASO RECURSIVO — problema más pequeño
        parte_del_problema,
        funcion_recursiva(resto_del_problema)
    )
```

Si te confundes, usa [Python Tutor](https://pythontutor.com/) para ver, paso a
paso, cómo se apilan las llamadas (literalmente usa una pila de llamadas,
el mismo concepto de `lab01_pila.py`).

## Instrucciones

Implementa las 5 funciones de `lab05_recursion.py` donde dice `# TODO`.

| Función | Qué practica |
|---------|---------------|
| `factorial(n)` | Recursión simple |
| `suma_lista_recursiva(lista)` | Recursión sobre una lista (`lista[0]` + `lista[1:]`) |
| `es_palindromo(texto)` | Recursión que compara extremos |
| `dividir_seguro(a, b)` | `try/except` para evitar que el programa se caiga |
| `obtener_elemento(lista, indice)` | `try/except` + `raise` para relanzar un error más claro |

## Autoevaluación

```bash
pip install pytest   # si no lo hiciste ya
pytest -q
```

## Siguiente paso

Ya completaste el refuerzo. Vuelve a
[`modulo-1-estructuras-lineales/semana-01/laboratorio/`](../../../modulo-1-estructuras-lineales/semana-01/laboratorio/)
y repite el Lab 1 del curso — ahora deberías poder implementar `Pila` sin
quedarte atascado en la sintaxis de Python.
