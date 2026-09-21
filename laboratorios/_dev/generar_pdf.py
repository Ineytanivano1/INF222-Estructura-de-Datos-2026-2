"""
Genera refuerzo-python/guia-rapida-python.pdf a partir del contenido
definido en este script.

Uso:
    python3 -m venv /tmp/pdfenv && /tmp/pdfenv/bin/pip install fpdf2
    /tmp/pdfenv/bin/python generar_pdf.py

Este script no forma parte del material del curso; es solo la herramienta
usada para producir el PDF. Se conserva para poder regenerarlo si cambia
el contenido.
"""
from fpdf import FPDF

INK = (27, 32, 48)
MUTED = (90, 97, 116)
AMBER = (122, 82, 16)
TEAL = (36, 87, 81)
CODE_BG = (35, 43, 62)
CODE_INK = (231, 233, 242)
LINE = (217, 213, 199)


class Guia(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*MUTED)
        self.cell(0, 8, "Guía rápida de Python -- INF 222 Estructura de Datos", align="L")
        self.cell(0, 8, f"{self.page_no()}", align="R")
        self.ln(10)
        self.set_draw_color(*LINE)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(4)

    def footer(self):
        pass

    def h1(self, text):
        self.set_font("Helvetica", "B", 20)
        self.set_text_color(*INK)
        self.cell(0, 12, text, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*AMBER)
        self.set_line_width(0.8)
        self.line(15, self.get_y(), 55, self.get_y())
        self.ln(6)

    def h2(self, text):
        if self.get_y() > 215:
            self.add_page()
        self.ln(2)
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(*TEAL)
        self.cell(0, 9, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def body(self, text):
        self.set_font("Helvetica", "", 10.5)
        self.set_text_color(*INK)
        self.multi_cell(0, 5.6, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def bullet(self, text):
        self.set_font("Helvetica", "", 10.5)
        self.set_text_color(*INK)
        x = self.get_x()
        self.cell(5, 5.6, "-")
        self.set_x(x + 5)
        self.multi_cell(0, 5.6, text, new_x="LMARGIN", new_y="NEXT")
        self.set_x(x)

    def code(self, text):
        self.ln(1)
        lines = text.strip("\n").split("\n")
        pad = 3
        line_h = 5.0
        block_h = pad * 2 + line_h * len(lines)
        if self.get_y() + block_h > 270:
            self.add_page()
        x0, y0 = self.get_x(), self.get_y()
        self.set_fill_color(*CODE_BG)
        self.rect(x0, y0, 180, block_h, style="F")
        self.set_xy(x0 + 4, y0 + pad)
        self.set_font("Courier", "", 9.3)
        self.set_text_color(*CODE_INK)
        for line in lines:
            self.cell(172, line_h, line, new_x="LMARGIN", new_y="NEXT")
            self.set_x(x0 + 4)
        self.set_xy(x0, y0 + block_h + 3)
        self.set_text_color(*INK)

    def table(self, headers, rows, widths):
        self.ln(1)
        if self.get_y() + 7 * (len(rows) + 1) > 275:
            self.add_page()
        self.set_font("Helvetica", "B", 9.5)
        self.set_fill_color(234, 231, 220)
        self.set_text_color(*INK)
        self.set_draw_color(*LINE)
        for h, w in zip(headers, widths):
            self.cell(w, 7, h, border=1, fill=True)
        self.ln()
        self.set_font("Courier", "", 8.6)
        for row in rows:
            for cell_text, w in zip(row, widths):
                self.cell(w, 7, str(cell_text), border=1)
            self.ln()
        self.ln(2)


pdf = Guia(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=True, margin=18)
pdf.set_margins(15, 15, 15)
pdf.set_title("Guía rápida de Python - INF 222")

# ---------------------------------------------------------------- Portada
pdf.add_page()
pdf.ln(60)
pdf.set_font("Helvetica", "B", 30)
pdf.set_text_color(*INK)
pdf.cell(0, 14, "Guía rápida de Python", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.set_font("Helvetica", "", 15)
pdf.set_text_color(*TEAL)
pdf.cell(0, 10, "Lo esencial para Estructura de Datos", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.ln(10)
pdf.set_font("Helvetica", "", 11)
pdf.set_text_color(*MUTED)
pdf.cell(0, 7, "INF 222 - Estructura de Datos - Semestre 2026-2", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.cell(0, 7, "Material de refuerzo -- no reemplaza el contenido oficial del curso", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.ln(20)
pdf.set_font("Helvetica", "I", 10)
pdf.multi_cell(0, 6,
    "Índice: 1) Variables y tipos  2) Operadores  3) Control de flujo  "
    "4) Funciones  5) Colecciones  6) Manejo de errores  "
    "7) Programación orientada a objetos  8) Recursión  9) Buenas prácticas  "
    "10) Sitios para seguir aprendiendo",
    align="C")

# ---------------------------------------------------------------- 1. Variables y tipos
pdf.add_page()
pdf.h1("1. Variables y tipos de datos")
pdf.body("Python no declara tipos: el tipo se infiere del valor asignado. Una misma "
         "variable puede cambiar de tipo (evita hacerlo a propósito, pero es válido).")
pdf.code(
    'edad = 20            # int\n'
    'altura = 1.75         # float\n'
    'nombre = "Ana"         # str\n'
    'activo = True          # bool\n'
    'nada = None            # ausencia de valor\n'
    'type(edad)             # <class \'int\'>\n'
    'type(edad).__name__    # "int"'
)
pdf.h2("Conversión entre tipos")
pdf.code(
    'int("5")     # 5\n'
    'float("3.2") # 3.2\n'
    'str(42)      # "42"\n'
    'int("abc")   # ValueError: invalid literal for int()'
)

pdf.h1("2. Operadores")
pdf.table(
    ["Tipo", "Operadores", "Ejemplo"],
    [
        ["Aritméticos", "+ - * / // % **", "7 // 2 -> 3   7 % 2 -> 1   2**10 -> 1024"],
        ["Comparación", "== != < > <= >=", "5 == 5 -> True"],
        ["Lógicos", "and or not", "edad >= 18 and activo"],
        ["Pertenencia", "in / not in", "3 in [1, 2, 3] -> True"],
        ["Asignación", "= += -= *= /=", "contador += 1"],
    ],
    [35, 45, 100],
)
pdf.h2("f-strings (formatear texto)")
pdf.code(
    'nombre = "Ana"\n'
    'edad = 20\n'
    'print(f"{nombre} tiene {edad} años")\n'
    'print(f"El doble es {edad * 2}")'
)

# ---------------------------------------------------------------- 3. Control de flujo
pdf.add_page()
pdf.h1("3. Control de flujo")
pdf.h2("if / elif / else")
pdf.code(
    'if edad < 13:\n'
    '    categoria = "niño"\n'
    'elif edad < 18:\n'
    '    categoria = "adolescente"\n'
    'else:\n'
    '    categoria = "adulto"'
)
pdf.body("Python usa indentación (4 espacios) en vez de llaves {} para marcar bloques. "
         "Un error de indentación es un error de sintaxis, no de estilo.")

pdf.h2("while (repite mientras la condición sea verdadera)")
pdf.code(
    'i = 1\n'
    'while i <= 5:\n'
    '    print(i)\n'
    '    i += 1   # sin esto: bucle infinito'
)

pdf.h2("for (recorre una secuencia)")
pdf.code(
    'for i in range(5):              # 0,1,2,3,4\n'
    '    print(i)\n\n'
    'for elemento in [10, 20, 30]:\n'
    '    print(elemento)\n\n'
    'for i, valor in enumerate(["a", "b"]):\n'
    '    print(i, valor)              # 0 a, 1 b'
)

pdf.h2("break / continue")
pdf.code(
    'for x in lista:\n'
    '    if x == buscado:\n'
    '        break        # sale del bucle ya\n\n'
    'for x in lista:\n'
    '    if x < 0:\n'
    '        continue      # salta al siguiente x\n'
    '    print(x)'
)

# ---------------------------------------------------------------- 4. Funciones
pdf.add_page()
pdf.h1("4. Funciones")
pdf.code(
    'def es_par(numero):\n'
    '    return numero % 2 == 0\n\n'
    'def saludar(nombre, saludo="Hola"):   # valor por defecto\n'
    '    return f"{saludo}, {nombre}!"\n\n'
    'def sumar(*numeros):                    # args variables\n'
    '    return sum(numeros)\n\n'
    'sumar(1, 2, 3)     # 6\n'
    'saludar("Ana")     # "Hola, Ana!"'
)
pdf.h2("Una función puede recibir otra función")
pdf.code(
    'def aplicar(lista, operacion):\n'
    '    return [operacion(x) for x in lista]\n\n'
    'aplicar([1, 2, 3], lambda x: x * 2)   # [2, 4, 6]'
)

# ---------------------------------------------------------------- 5. Colecciones
pdf.h1("5. Colecciones nativas")
pdf.table(
    ["Tipo", "Sintaxis", "Modificable", "Uso típico"],
    [
        ["list", "[1, 2, 3]", "Sí", "Secuencia que cambia (Pila, Cola)"],
        ["tuple", "(x, y)", "No", "Datos fijos, ej. coordenadas"],
        ["dict", '{"k": v}', "Sí", "Buscar por clave"],
        ["set", "{1, 2, 3}", "Sí", "Pertenencia rápida, sin duplicados"],
    ],
    [22, 38, 30, 90],
)
pdf.h2("Métodos de listas más usados")
pdf.code(
    'p = []\n'
    'p.append(10)     # agrega al final -- O(1)\n'
    'p.pop()           # quita y retorna el último -- O(1)\n'
    'p.insert(0, 99)   # inserta en una posición -- O(n)\n'
    'p[-1]              # último elemento\n'
    'p[1:3]             # slicing: sub-lista\n'
    'len(p)             # tamaño'
)
pdf.h2("Diccionarios")
pdf.code(
    'frecuencias = {}\n'
    'frecuencias["a"] = frecuencias.get("a", 0) + 1\n'
    'for clave, valor in frecuencias.items():\n'
    '    print(clave, valor)'
)

# ---------------------------------------------------------------- 6. Errores
pdf.add_page()
pdf.h1("6. Manejo de errores")
pdf.code(
    'def pop(self):\n'
    '    if self.is_empty():\n'
    '        raise IndexError("pop en pila vacía")\n'
    '    return self._datos.pop()\n\n'
    'try:\n'
    '    pila.pop()\n'
    'except IndexError:\n'
    '    print("La pila estaba vacía")'
)
pdf.h2("Excepciones comunes")
pdf.table(
    ["Excepción", "Cuándo ocurre"],
    [
        ["IndexError", "Índice fuera de rango en una lista"],
        ["KeyError", "Clave inexistente en un diccionario"],
        ["ValueError", 'Valor de tipo correcto pero inválido, ej. int("abc")'],
        ["TypeError", "Operación entre tipos incompatibles"],
        ["ZeroDivisionError", "División entre cero"],
    ],
    [45, 135],
)

# ---------------------------------------------------------------- 7. POO
pdf.add_page()
pdf.h1("7. Programación orientada a objetos")
pdf.body("self es el objeto sobre el que se llamó el método; Python lo pasa "
         "automáticamente. __init__ es el constructor: corre una vez, al crear "
         "el objeto.")
pdf.code(
    'class Pila:\n'
    '    def __init__(self):\n'
    '        self._datos = []          # atributo\n\n'
    '    def push(self, dato):          # método\n'
    '        self._datos.append(dato)\n\n'
    '    def pop(self):\n'
    '        if not self._datos:\n'
    '            raise IndexError("pila vacía")\n'
    '        return self._datos.pop()\n\n'
    '    def __str__(self):              # usado por print()\n'
    '        return f"Pila: {self._datos}"\n\n'
    'p = Pila()\n'
    'p.push(10)\n'
    'print(p)          # Pila: [10]'
)

# ---------------------------------------------------------------- 8. Recursión
pdf.h1("8. Recursión")
pdf.code(
    'def funcion(problema):\n'
    '    if es_caso_base(problema):        # 1. CASO BASE\n'
    '        return valor_directo\n'
    '    return combinar(                    # 2. CASO RECURSIVO\n'
    '        parte, funcion(resto_del_problema)\n'
    '    )\n\n'
    'def factorial(n):\n'
    '    if n == 0:\n'
    '        return 1\n'
    '    return n * factorial(n - 1)'
)
pdf.body("Sin caso base: recursión infinita -> RecursionError. "
         "Usa pythontutor.com para ver, paso a paso, cómo se apilan las llamadas.")

# ---------------------------------------------------------------- 9. Buenas prácticas
pdf.add_page()
pdf.h1("9. Buenas prácticas rápidas (PEP 8)")
pdf.bullet("Nombres de variables y funciones: snake_case (minúsculas_con_guion_bajo).")
pdf.bullet("Nombres de clases: PascalCase (PrimeraLetraMayúscula), ej. ListaEnlazada.")
pdf.bullet("Indentación: 4 espacios, nunca mezclar con tabs.")
pdf.bullet("Un solo import por línea; imports arriba del archivo.")
pdf.bullet("Nombres descriptivos: 'contador' en vez de 'c', 'lista_numeros' en vez de 'l'.")
pdf.bullet("Comentarios: explican el POR QUÉ, no el QUÉ (el código ya dice qué hace).")

# ---------------------------------------------------------------- 10. Sitios
pdf.h1("10. Sitios reales para seguir aprendiendo")
pdf.table(
    ["Sitio", "Para qué sirve"],
    [
        ["docs.python.org/es/3/tutorial", "Tutorial oficial de Python, en español"],
        ["pythontutor.com", "Visualiza paso a paso la ejecución y la memoria"],
        ["w3schools.com/python", "Referencia corta con editor interactivo"],
        ["realpython.com", "Artículos y tutoriales más profundos"],
        ["programiz.com/python-programming", "Lecciones cortas, buen repaso pre-parcial"],
        ["py4e.com", "Curso completo Python for Everybody, gratuito"],
        ["cs50.harvard.edu/python", "Curso universitario completo (Harvard/edX)"],
        ["exercism.org/tracks/python", "Ejercicios cortos con retroalimentación"],
    ],
    [70, 110],
)
pdf.ln(4)
pdf.set_font("Helvetica", "I", 9.5)
pdf.set_text_color(*MUTED)
pdf.multi_cell(0, 5.5,
    "Siguiente paso: resuelve los laboratorios lab00 a lab05 en "
    "refuerzo-python/laboratorios/, en orden, corriendo pytest en cada uno.")

pdf.output("../guia-rapida-python.pdf")
print("PDF generado.")
