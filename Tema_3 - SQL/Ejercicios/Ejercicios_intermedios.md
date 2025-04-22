## Ejercicios intermedios de SQL

### 1.Consulta con JOIN
Muestra el nombre de los clientes y el número de teléfono asociado a cada uno.

<details>
  <summary>Solución</summary>
  
  ```sql
    SELECT c.nombre, t.numero
    FROM CLIENTE c
    JOIN TELEFONO t ON c.dni = t.cliente;
  ```
  
</details>

### 2.Consulta con funciones de agregación

Calcula el promedio de puntos acumulados por los teléfonos de la compañía **A00000001**.

<details>
  <summary>Solución</summary>
  
  ```sql
    SELECT AVG(puntos) AS promedio_puntos
    FROM TELEFONO
    WHERE compañia = 'A00000001';
  ```
  
</details>

### 3.Subconsulta

Encuentra los nombres de los clientes que tienen un teléfono con más de 20,000 puntos.

<details>
  <summary>Solución</summary>
  
  ```sql
    SELECT nombre
    FROM CLIENTE
    WHERE dni IN (
        SELECT cliente
        FROM TELEFONO
        WHERE puntos > 20000
    );
  ```
  
</details>