# Tema 0: Fundamentos de Python - Módulo 4

## 📌 Bucles en Python

Los **bucles** permiten ejecutar un bloque de código varias veces. Son muy útiles para automatizar tareas repetitivas.

---

### 🔁 Bucle `for`

Se utiliza para recorrer elementos de una secuencia (como listas, cadenas, rangos, etc.).

- En el siguiente ejemplo range(5) genera los números del 0 al 4.

```python
for numero in range(5):
    print(numero)
```

### 🔁 Bucle `while`


```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```
- ⚠️ Cuidado con los bucles infinitos: asegúrate de que la condición se rompa en algún momento.

## 📌 if y Comparadores (Operadores de comparación)

El if es una estructura condicional que permite ejecutar un bloque de código solo si se cumple una condición.

El bloque de codigo dentro de la palabra reservada `elif` se ejecutara siempre y cuando no se cumplan la condicion anterior y ademas se cumpla la condicion expresada en el mismo


El bloque de codigo dentro de la palabra reservada `else` se ejecutara siempre y cuando no se cumplan ninguna de las condiciones anteriores

```python
nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprobado")
else:
    print("Reprobado")
```

| Operador | Significado         | Ejemplo  | Resultado |
|----------|---------------------|----------|-----------|
| `==`     | Igual a             | `5 == 5` | `True`    |
| `!=`     | Distinto de         | `5 != 3` | `True`    |
| `>`      | Mayor que           | `7 > 3`  | `True`    |
| `<`      | Menor que           | `2 < 1`  | `False`   |
| `>=`     | Mayor o igual que   | `4 >= 4` | `True`    |
| `<=`     | Menor o igual que   | `5 <= 2` | `False`   |
