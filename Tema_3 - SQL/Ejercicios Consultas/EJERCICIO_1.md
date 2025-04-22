## Ejercicio 1: DML (Data Manipulation Language)

Realiza las siguientes operaciones en la tabla CLIENTE:

### 1.Inserta un nuevo cliente con los siguientes datos:
**DNI:** 98765432B
**Nombre:** Sofía López
**Fecha de nacimiento:** 15/05/1995
**Dirección:** C/ Ejemplo nº 2
**CP:** 28002
**Ciudad:** Madrid
**Provincia:** Madrid

<details>
  <summary>Solución</summary>
  
  ```sql
    INSERT INTO CLIENTE (dni, nombre, f_nac, direccion, cp, ciudad, provincia)
    VALUES ('98765432B', 'Sofía López', '1995-05-15', 'C/ Ejemplo nº 2', '28002', 'Madrid', 'Madrid');
  ```
  
</details>

### 2.Actualiza la dirección del cliente con DNI 35000001P a C/ Nueva Melancolía nº 10.

<details>
  <summary>Solución</summary>
  
  ```sql
    UPDATE CLIENTE
    SET direccion = 'C/ Nueva Melancolía nº 10'
    WHERE dni = '35000001P';
  ```
  
</details>

### 3.Elimina el cliente con DNI 12000002Q.

<details>
  <summary>Solución</summary>
  
  ```sql
    DELETE FROM CLIENTE
    WHERE dni = '12000002Q';
  ```
  
</details>