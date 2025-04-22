## Ejercicio 2: DDL (Data Definition Language)

Trabaja con la estructura de la base de datos:

### 1.Crea una nueva tabla llamada **FACTURA** con las siguientes columnas:

**id_factura** (número, clave primaria)
**cliente** (char(9), clave foránea que referencia a **CLIENTE.dni**)
**monto** (número con 2 decimales, no nulo)
**fecha** (fecha, no nula).

<details>
  <summary>Solución</summary>
  
  ```sql
    CREATE TABLE FACTURA (
        id_factura NUMBER PRIMARY KEY,
        cliente CHAR(9),
        monto NUMBER(10, 2) NOT NULL,
        fecha DATE NOT NULL,
        CONSTRAINT fk_cliente FOREIGN KEY (cliente) REFERENCES CLIENTE(dni)
    );
  ```
  
</details>

### 2.Agrega una nueva columna llamada **email** a la tabla **CLIENTE**.

<details>
  <summary>Solución</summary>
  
  ```sql
    ALTER TABLE CLIENTE
    ADD email VARCHAR2(100);
  ```
  
</details>

### 3.Elimina la tabla FACTURA creada anteriormente.

<details>
  <summary>Solución</summary>
  
  ```sql
    DROP TABLE FACTURA;
  ```
  
</details>