# Lab 2 (refuerzo) — Funciones

**Material de refuerzo de Python · No cuenta para la nota del curso**

---

## Objetivo

Practicar `def`, parámetros, `return`, valores por defecto, `*args` y pasar
funciones como parámetros. Todos los métodos de `Pila`, `Cola`, `ListaEnlazada`
etc. que vas a construir en el curso son, en el fondo, funciones dentro de
una clase — dominar esto primero hace todo lo demás más fácil.

## Instrucciones

Implementa las 5 funciones de `lab02_funciones.py` donde dice `# TODO`.

| Función | Qué practica |
|---------|---------------|
| `es_primo(n)` | Lógica con `return` anticipado |
| `potencia(base, exponente=2)` | Parámetro con valor por defecto |
| `sumar_todos(*numeros)` | Número variable de argumentos (`*args`) |
| `crear_mensaje(nombre, saludo="Hola")` | Otro valor por defecto + f-strings |
| `aplicar_operacion(lista, operacion)` | Pasar una función como parámetro |

## Autoevaluación

```bash
pip install pytest   # si no lo hiciste ya
pytest -q
```

## Siguiente paso

Continúa con [`../lab03_listas_tuplas_diccionarios/`](../lab03_listas_tuplas_diccionarios/).
