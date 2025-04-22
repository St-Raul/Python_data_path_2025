# Tema 0: Fundamentos de Python - Módulo 5

## 📌 ¿Qué es una función?

Una **función** es un bloque de código reutilizable que ejecuta una tarea específica.  
Las funciones nos ayudan a escribir código más limpio, ordenado y reutilizable.

---

### ➤ Cómo definir una función

Usamos la palabra clave `def` para crear funciones en Python.

```python
def nombre_de_la_funcion():
    print("Hola, bienvenido/a al curso de Python")
```

### ➤ Llamar a la función

```python
nombre_de_la_funcion()
```

## 📌 Argumentos y Parámetros

Las funciones pueden recibir datos a través de argumentos, que se definen dentro de los paréntesis.

```python
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Ana")
```

### ➤ Argumentos Multiples 

Puedes pasar más de un argumento separándolos con comas.

```python
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)  # 8
```

### ➤ Valores por defecto

Puedes definir valores por defecto para argumentos opcionales

```python
def saludar(nombre="invitado"):
    print(f"Hola, {nombre}")

saludar()          # Hola, invitado
saludar("Carlos")  # Hola, Carlos
```

### ➤ Valor de retorno (return)

La palabra clave return permite que una función devuelva un valor para usarlo más adelante.

```python
def cuadrado(numero):
    return numero * numero

resultado = cuadrado(4)
print(resultado)  # 16
```