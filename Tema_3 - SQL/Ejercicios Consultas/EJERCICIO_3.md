## Ejercicio 3: DCL (Data Control Language)

Gestiona los permisos de acceso a las tablas:

### 1.Otorga permisos de selección sobre la tabla **CLIENTE** al usuario **usuario1**.

<details>
  <summary>Solución</summary>
  
  ```sql
    GRANT SELECT ON CLIENTE TO usuario1;
  ```
  
</details>

### 2.Otorga permisos de inserción y actualización sobre la tabla **TELEFONO** al usuario **usuario2**.

<details>
  <summary>Solución</summary>
  
  ```sql
    GRANT INSERT, UPDATE ON TELEFONO TO usuario2;
  ```
  
</details>

### 3.Revoca todos los permisos sobre la tabla **CLIENTE** al usuario **usuario1**.

<details>
  <summary>Solución</summary>
  
  ```sql
    REVOKE ALL ON CLIENTE FROM usuario1;
  ```
  
</details>