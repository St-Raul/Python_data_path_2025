# Tema 0: Fundamentos de Python - Modulo 2

## 📌 Variables

Las **variables** son nombres que se usan para almacenar datos en la memoria. Son fundamentales para guardar información y reutilizarla en el código.

### ➤ Caracteristicas de las variable en Python:

- No necesitas declarar el tipo de variable.

- Python asigna el tipo según el valor que contenga.

### ➤ Cómo declarar una variable en Python:

```python
nombre = "Ana"
edad = 25
```
## 📌 Tipos de Datos

(En profundidad en el modulo 3)

| Tipo de dato       | Representación     | Declaración                      |
|------------------  |--------------------|----------------------------------|
| Número entero      | `10`               | `int`                            |
| Número decimal     | `3.14`             | `float`                          |
| Cadena de texto    | `"Hola"`           | `str`                            |
| Valor booleano     | `True`, `False`    | `bool`                           |
| Lista de elementos | `[1, 2, 3]`        | `list`                           |
| Diccionario        | `{"a": 1}`         | `dict`                           |

## 📌 Conversión de Tipos (Casting)

A veces necesitas convertir un dato de un tipo a otro, por ejemplo, de cadena a número.

### ➤ Ejemplos de conversión:

```python
# De string a entero
numero = int("10")

# De entero a string
texto = str(123)

# De entero a float
decimal = float(7)

# De número a booleano
verdadero = bool(1)  # True
falso = bool(0)      # False
```
## 📌 Formatos de Salida (f-strings)

- Para mostrar información en pantalla de forma clara, usamos los f-strings o formato de cadenas.

- Con f"" puedes insertar variables directamente dentro de una cadena.

### ➤ Ejemplos de conversión:

```python
nombre = "Ana"
edad = 25
print(f"Hola, me llamo {nombre} y tengo {edad} años.")
```

