# Tema 0: Fundamentos de Python - Módulo 6

## 🧱 Programación Orientada a Objetos en Python

La Programación Orientada a Objetos (OOP) permite modelar conceptos del mundo real usando **clases** y **objetos**.

---

## 📌 Clases

Una **clase** es un molde para crear objetos. Define las propiedades (atributos) y comportamientos (métodos) que tendrán los objetos que se creen a partir de ella.

### ➤ Sintaxis básica para crear una clase:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")



## 📌 Métodos
Los métodos son funciones definidas dentro de una clase. Describen el comportamiento de un objeto.

### ➤ Ejemplo:

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

ana = Persona("Ana")
ana.saludar()  # Hola, soy Ana
```



## 📌 Atributos

Los **atributos** son variables que pertenecen a un objeto. Describen sus características.

### ➤ Ejemplo:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # atributo
        self.edad = edad      # atributo

ana = Persona("Ana", 30)
print(ana.nombre)  # Ana
```


## 📌 Herencia
La herencia permite crear una clase nueva basada en otra existente. La clase hija hereda atributos y métodos de la clase padre.


### ➤ Ejemplo:

```python
class Animal:
    def hablar(self):
        print("Hace un sonido")

class Perro(Animal):
    def hablar(self):
        print("Ladra")

mi_perro = Perro()
mi_perro.hablar()  # Ladra
```


## 📌 Polimorfismo
El polimorfismo permite que diferentes clases respondan de manera distinta al mismo método.

### ➤ Ejemplo:

```python
class Gato:
    def hablar(self):
        print("Miau")

class Perro:
    def hablar(self):
        print("Guau")

def hacer_hablar(animal):
    animal.hablar()

hacer_hablar(Gato())   # Miau
hacer_hablar(Perro())  # Guau
```
