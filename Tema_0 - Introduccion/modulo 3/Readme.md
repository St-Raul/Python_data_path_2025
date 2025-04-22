# Tema 0: Fundamentos de Python - Módulo 3

## 📌 Diccionarios

Un **diccionario** en Python es una colección de datos que almacena pares clave:valor. Es muy útil para representar objetos o estructuras con atributos.

### ➤ Cómo declarar un diccionario:

```python
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Lima"
}
```

### ➤ Cómo declarar un diccionario:

- Las claves (keys) son únicas.

- Los valores pueden ser de cualquier tipo de dato.

### ➤ Acceder a valores:

```python
print(persona["nombre"])
```
## 📌 Metodos de un diccionario

Los métodos son funciones asociadas a un objeto, y permiten manipularlo o consultarlo.

| Método            | Descripción                                  | Ejemplo                                 |
|-------------------|----------------------------------------------|-----------------------------------------|
| `get(clave)`      | Obtiene el valor de una clave                | `persona.get("nombre")` → `"Ana"`       |
| `keys()`          | Devuelve las claves del diccionario          | `persona.keys()`                        |
| `values()`        | Devuelve los valores                         | `persona.values()`                      |
| `items()`         | Devuelve clave:valor como tuplas             | `persona.items()`                       |
| `update({...})`   | Actualiza el diccionario con nuevos datos    | `persona.update({"edad": 30})`          |
| `pop(clave)`      | Elimina una clave y devuelve su valor        | `persona.pop("ciudad")`                 |


## 📌 Propiedades de Diccionarios

Una propiedad en Python es una característica o atributo de un objeto que describe algún aspecto de él, como su longitud, contenido o existencia de elementos.
A diferencia de los métodos, no se llama con paréntesis y no modifica el objeto.

| Propiedad      | Descripción                                     | Ejemplo                         |
|----------------|-------------------------------------------------|---------------------------------|
| Longitud       | Número de elementos (pares clave:valor)         | `len(persona)` → `3`            |
| Comprobación   | Verificar si una clave existe                   | `"nombre" in persona` → `True`  |
