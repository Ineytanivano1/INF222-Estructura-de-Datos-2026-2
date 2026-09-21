# Lab 3 (refuerzo) — Listas, tuplas, diccionarios y sets

**Material de refuerzo de Python · No cuenta para la nota del curso**

---

## Objetivo

Dominar las 4 colecciones nativas de Python y cuándo usar cada una.
Esto es directamente relevante: en `semana-01/laboratorio/lab01_pila.py`
la clase `Pila` usa una **lista** como contenedor interno (`self._datos = []`).

## Cuándo usar cada una (referencia rápida)

| Colección | Ordenada | Modificable | Duplicados | Úsala cuando... |
|-----------|----------|-------------|------------|------------------|
| `list` | Sí | Sí | Sí | Necesitas una secuencia que cambia (como en `Pila`, `Cola`) |
| `tuple` | Sí | No | Sí | Datos que no deben cambiar, ej. coordenadas `(x, y)` |
| `dict` | Sí (inserción) | Sí | Claves únicas | Necesitas buscar por clave, no por posición |
| `set` | No | Sí | No | Necesitas pertenencia rápida o quitar duplicados |

## Instrucciones

Implementa las 5 funciones de `lab03_colecciones.py` donde dice `# TODO`.

| Función | Colección clave |
|---------|-----------------|
| `invertir_lista(lista)` | `list` + slicing |
| `eliminar_duplicados(lista)` | `list` + `set` auxiliar |
| `combinar_en_tupla(a, b)` | `tuple` + `zip()` |
| `contar_frecuencias(palabras)` | `dict` |
| `interseccion(a, b)` | `set` |

## Autoevaluación

```bash
pip install pytest   # si no lo hiciste ya
pytest -q
```

## Siguiente paso

Continúa con [`../lab04_clases_y_objetos/`](../lab04_clases_y_objetos/) — ahí
construyes tu primera clase, el paso previo directo a `Pila` de semana 1.
