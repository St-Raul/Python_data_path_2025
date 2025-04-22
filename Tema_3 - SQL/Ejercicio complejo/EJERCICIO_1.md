## Análisis de llamadas y facturación
Crea una consulta que muestre el nombre del cliente, el número de teléfono, la cantidad total de llamadas realizadas y la duración total de esas llamadas (en minutos). Solo incluye clientes que hayan realizado más de 5 llamadas en total.

<details>
  <summary>Solución</summary>
  
  ```sql
    SELECT c.nombre, t.numero, COUNT(l.tf_origen) AS total_llamadas, SUM(l.duracion) / 60 AS duracion_total_minutos
    FROM CLIENTE c
    JOIN TELEFONO t ON c.dni = t.cliente
    JOIN LLAMADA l ON t.numero = l.tf_origen
    GROUP BY c.nombre, t.numero
    HAVING COUNT(l.tf_origen) > 5;
  ```
  
</details>