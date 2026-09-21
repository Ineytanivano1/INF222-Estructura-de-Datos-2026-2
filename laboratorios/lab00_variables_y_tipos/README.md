# Lab 0 (refuerzo) — Variables, tipos de datos y operadores

**Material de refuerzo de Python · No cuenta para la nota del curso**

---

## Objetivo

Practicar variables, tipos básicos (`int`, `float`, `str`, `bool`), operadores y f-strings:
la base mínima para leer y escribir cualquier línea de código Python.

## Antes de empezar

- Lee las diapositivas 4-6 de `../../presentacion-python-express.html`.
- Ten a mano `../../guia-rapida-python.pdf` (sección "Tipos y operadores").

## Instrucciones

Abre `lab00_variables.py` e implementa las 4 funciones donde dice `# TODO`.
No cambies el nombre de las funciones ni sus parámetros.

| Función | Qué hace |
|---------|----------|
| `resumen_numero(n)` | Analiza un número: par/impar, signo, cuadrado y tipo |
| `celsius_a_fahrenheit(c)` | Convierte temperatura |
| `promedio(lista)` | Promedio de una lista, sin romperse con lista vacía |
| `describir_persona(nombre, edad)` | Arma un string con f-strings |

## Autoevaluación

Desde esta carpeta:

```bash
pip install pytest        # una sola vez
pytest -q
```

Cuando los 6 tests pasen (`6 passed`), dominas esta parte. Si algo falla,
lee el mensaje de pytest: te dice exactamente qué esperaba y qué obtuvo.

## Siguiente paso

Continúa con [`../lab01_control_de_flujo/`](../lab01_control_de_flujo/).
