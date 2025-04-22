# Tema 0: Fundamentos de Python - Módulo 1

## 📌 ¿Qué es un String?

Un **string** (o cadena de texto) es una secuencia de caracteres encerrados entre comillas. Puede contener letras, números, espacios y símbolos.

### ➤ Cómo declarar un string en Python:

```python
mensaje = "Hola mundo"
nombre = 'Ana'
```

### ➤ Caracteristicas

- Puedes usar comillas simples ' o dobles " indistintamente.

- Para textos largos, puedes usar comillas triples (''' o """).

- Son inmutables (no se pueden modificar una vez creados).

- Se pueden recorrer como una secuencia (como una lista).

- Puedes acceder a sus caracteres por índice.

| Operación              | Ejemplo                                      | Resultado        |
|------------------------|----------------------------------------------|------------------|
| Concatenar             | `"Hola" + " Mundo"`                          | `"Hola Mundo"`   |
| Repetir                | `"Hola" * 3`                                 | `"HolaHolaHola"` |
| Longitud               | `len("Python")`                              | `6`              |
| Mayúsculas             | `"hola".upper()`                             | `"HOLA"`         |
| Minúsculas             | `"PYTHON".lower()`                           | `"python"`       |
| Capitalizar            | `"python".capitalize()`                      | `"Python"`       |
| Reemplazar texto       | `"Hola mundo".replace("mundo", "Python")`    | `"Hola Python"`  |
| Cortar texto (slicing) | `"Python"[0:3]`                              | `"Pyt"`          |
