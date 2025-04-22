# SQL, ¿qué es SQL?

SQL (Structured Query Language) es un lenguaje estándar para interactuar con bases de datos relacionales. Permite realizar operaciones como consultar, insertar, actualizar y eliminar datos, así como administrar la estructura de las bases de datos. Es ampliamente utilizado en aplicaciones empresariales, desarrollo web y análisis de datos debido a su capacidad para manejar grandes volúmenes de información de manera eficiente.

## Un poco de historia

SQL fue desarrollado en la década de 1970 por IBM como parte del proyecto System R, un sistema de base de datos relacional basado en el modelo propuesto por Edgar F. Codd. En 1986, SQL se convirtió en un estándar de la ANSI (American National Standards Institute) y, posteriormente, en un estándar ISO. Desde entonces, ha evolucionado y se ha convertido en el lenguaje principal para trabajar con bases de datos relacionales.

Entre las bases de datos más destacadas que utilizan SQL se encuentra **Oracle Database**, una de las bases de datos relacionales más robustas y ampliamente adoptadas en el mundo empresarial.

## ¿En qué se basa?

SQL se basa en el modelo relacional, que organiza los datos en tablas (también conocidas como relaciones). Cada tabla está compuesta por filas (registros) y columnas (atributos). Este modelo permite realizar operaciones complejas de consulta y manipulación de datos de manera estructurada.

## Funciones principales

SQL incluye una amplia gama de funcionalidades, entre las que destacan:

- **Consultas de datos**: Recuperar información de una o varias tablas mediante `SELECT`.
- **Inserción de datos**: Agregar nuevos registros a las tablas con `INSERT`.
- **Actualización de datos**: Modificar registros existentes usando `UPDATE`.
- **Eliminación de datos**: Borrar registros de las tablas con `DELETE`.
- **Creación y modificación de estructuras**: Crear, modificar y eliminar tablas y otros objetos de la base de datos mediante `CREATE`, `ALTER` y `DROP`.
- **Control de acceso**: Gestionar permisos y usuarios con `GRANT` y `REVOKE`.
- **Transacciones**: Asegurar la integridad de los datos mediante `COMMIT` y `ROLLBACK`.

## Tipos de consultas en SQL

En SQL, las consultas se pueden clasificar en tres categorías principales según su propósito y funcionalidad:

### 1. DML (Data Manipulation Language)
El lenguaje de manipulación de datos (DML) se utiliza para trabajar con los datos almacenados en las tablas. Estas consultas permiten insertar, actualizar, eliminar y recuperar datos. Algunos ejemplos de comandos DML son:

- **`SELECT`**: Recuperar datos de una o más tablas.
- **`INSERT`**: Agregar nuevos registros a una tabla.
- **`UPDATE`**: Modificar registros existentes en una tabla.
- **`DELETE`**: Eliminar registros de una tabla.

Ejemplo:
```sql
-- Insertar un nuevo registro
INSERT INTO Empleados (ID, Nombre, Departamento, Salario)
VALUES (2, 'Adrian Gómez', 'Data', 42000);

-- Actualizar un registro
UPDATE Empleados
SET Salario = 45000
WHERE ID = 2;

-- Eliminar un registro
DELETE FROM Empleados
WHERE ID = 2;
```

### 2. DDL (Data Definition Language)
El lenguaje de definición de datos (DDL) se utiliza para definir y modificar la estructura de las bases de datos y sus objetos, como tablas, índices y vistas. Algunos ejemplos de comandos DDL son:

- **`CREATE`**: Crear nuevos objetos en la base de datos (tablas, vistas, índices, etc.).
- **`ALTER`**: Modificar la estructura de un objeto existente.
- **`DROP`**: Eliminar un objeto de la base de datos.
- **`TRUNCATE`**: Eliminar todos los registros de una tabla sin afectar su estructura.

Ejemplo:
```sql
-- Crear una nueva tabla
CREATE TABLE Departamentos (
    ID NUMBER PRIMARY KEY,
    Nombre VARCHAR2(50)
);

-- Modificar una tabla existente
ALTER TABLE Empleados
ADD FechaContratacion DATE;

-- Eliminar una tabla
DROP TABLE Departamentos;
```

### 3. DCL (Data Control Language)
El lenguaje de control de datos (DCL) se utiliza para gestionar los permisos y el acceso a los datos en la base de datos. Algunos ejemplos de comandos DCL son:

- **`GRANT`**: Otorgar permisos a usuarios o roles.
- **`REVOKE`**: Revocar permisos previamente otorgados.


Ejemplo:
```sql
-- Otorgar permisos de selección a un usuario
GRANT SELECT ON Empleados TO usuario1;

-- Revocar permisos de selección a un usuario
REVOKE SELECT ON Empleados FROM usuario1;
```

Estos tipos de consultas permiten gestionar tanto los datos como la estructura y la seguridad de las bases de datos, proporcionando un control completo sobre el sistema de gestión de bases de datos.

## ¿Para qué se usa SQL?

SQL es ideal para:

- **Gestión de bases de datos**: Crear y administrar bases de datos relacionales.
- **Análisis de datos**: Consultar y resumir grandes volúmenes de datos.
- **Integración de aplicaciones**: Conectar aplicaciones con bases de datos para almacenar y recuperar información.
- **Automatización de procesos**: Crear procedimientos almacenados y disparadores para automatizar tareas repetitivas.

## Mejores casos de uso

SQL es especialmente útil en los siguientes escenarios:

1. **Gestión empresarial**: Manejar datos de clientes, ventas, inventarios y más.
2. **Análisis de datos**: Realizar consultas complejas para obtener insights de los datos.
3. **Desarrollo web**: Conectar aplicaciones web con bases de datos para almacenar información de usuarios, productos, etc.
4. **Sistemas financieros**: Gestionar transacciones y datos financieros.
5. **Big Data**: Trabajar con grandes volúmenes de datos en sistemas relacionales.

## SQL y Oracle Database

**Oracle Database** es una de las bases de datos más avanzadas y confiables que utiliza SQL como lenguaje principal. Ofrece características como:

- **Alta escalabilidad**: Ideal para grandes volúmenes de datos.
- **Soporte para PL/SQL**: Una extensión de SQL que permite crear procedimientos almacenados y funciones.
- **Seguridad avanzada**: Gestión de usuarios, roles y permisos.
- **Optimización de consultas**: Mejora del rendimiento en consultas complejas.

## Instalación

Para usar SQL, necesitas un sistema de gestión de bases de datos (DBMS). Algunos de los más populares son:

- **MySQL**: [Descargar MySQL](https://www.mysql.com/)
- **PostgreSQL**: [Descargar PostgreSQL](https://www.postgresql.org/)
- **SQLite**: [Descargar SQLite](https://www.sqlite.org/)
- **Microsoft SQL Server**: [Descargar SQL Server](https://www.microsoft.com/sql-server)

Para trabajar con SQL en Oracle Database, puedes descargar e instalar Oracle Database Express Edition (XE), una versión gratuita y ligera de Oracle:

- [Descargar Oracle Database XE](https://www.oracle.com/database/technologies/appdev/xe.html)

## Ejemplo básico con Oracle SQL

Aquí tienes un ejemplo básico de cómo usar SQL en Oracle para crear una tabla, insertar datos y realizar una consulta:

```sql
-- Crear una tabla
CREATE TABLE Empleados (
    ID NUMBER PRIMARY KEY,
    Nombre VARCHAR2(50),
    Departamento VARCHAR2(50),
    Salario NUMBER
);

-- Insertar datos
INSERT INTO Empleados (ID, Nombre, Departamento, Salario)
VALUES (1, 'Adrian Gómez', 'Data', 50000);

-- Consultar datos
SELECT Nombre, Salario
FROM Empleados
WHERE Salario > 40000;
```

## Visualización de datos con SQL y herramientas externas

SQL puede integrarse con herramientas como Oracle SQL Developer para ejecutar consultas y visualizar datos de manera gráfica. También puedes usar lenguajes como Python para interactuar con Oracle Database:

```python
import cx_Oracle

# Conectar a la base de datos
conn = cx_Oracle.connect("usuario", "contraseña", "localhost/XEPDB1")

# Crear un cursor
cursor = conn.cursor()

# Ejecutar una consulta
cursor.execute("SELECT * FROM Empleados")

# Mostrar los resultados
for row in cursor:
    print(row)

# Cerrar la conexión
conn.close()

```
## Recursos adicionales

- [Documentación oficial de SQL](https://www.w3schools.com/sql/)
- [Documentación de Oracle Database](https://docs.oracle.com/en/database/)
- [Descargar Oracle Database XE](https://www.oracle.com/database/technologies/appdev/xe.html)
