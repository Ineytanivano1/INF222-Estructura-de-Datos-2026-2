# Lab 1 (refuerzo) — Control de flujo

**Material de refuerzo de Python · No cuenta para la nota del curso**

---

## Objetivo

Dominar `if/elif/else`, `while`, `for` + `range()`, y `break`/`continue`.
Estas cuatro construcciones son el 80% de la lógica que vas a escribir en
cualquier estructura de datos (recorrer una pila, buscar en una lista, etc.).

## Instrucciones

Implementa las 5 funciones de `lab01_control_flujo.py` donde dice `# TODO`.
Cada una está pensada para forzarte a usar una construcción específica
(lee el docstring de cada función).

| Función | Construcción a practicar |
|---------|--------------------------|
| `clasificar_edad(edad)` | `if / elif / else` |
| `contar_hasta(n)` | `while` |
| `suma_pares(n)` | `for` + `range()` |
| `primer_multiplo(numero, limite)` | `for` + `break` |
| `solo_positivos(lista)` | `for` + `continue` |

## Autoevaluación

```bash
pip install pytest   # si no lo hiciste ya
pytest -q
```

## Siguiente paso

Continúa con [`../lab02_funciones/`](../lab02_funciones/).
