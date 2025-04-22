## Ejercicios básicos de SQL

### 1.Seleccionar todos los datos de una tabla

Escribe una consulta para mostrar todos los registros de la tabla CLIENTE.

<details>
  <summary>Solución</summary>
  
  ```sql
    SELECT * FROM CLIENTE;
  ```
  
</details>

### 2.Filtrar datos por una condición

Encuentra todos los clientes que viven en la ciudad de "Madrid".

<details>
  <summary>Solución</summary>
  
  ```sql
    SELECT * FROM CLIENTE
    WHERE ciudad = 'Madrid';
  ```
  
</details>

### 3.Ordenar resultados

Muestra los nombres de los clientes ordenados alfabéticamente.

<details>
  <summary>Solución</summary>
  
  ```sql
    SELECT nombre FROM CLIENTE
    ORDER BY nombre ASC;
  ```
  
</details>