# Transformaciones

Las transformaciones de datos son un paso fundamental en el análisis y preparación de datos. Consisten en modificar, reorganizar o limpiar los datos para que estén en un formato adecuado para el análisis o modelado. A continuación, se explican algunos conceptos básicos y ejemplos prácticos.

## ¿Qué son las transformaciones de datos?

Las transformaciones de datos implican aplicar operaciones a los datos para:

1. **Limpiar datos**: Eliminar valores nulos, duplicados o inconsistencias.
2. **Reformatear datos**: Cambiar el formato de columnas, como convertir fechas o cadenas a números.
3. **Crear nuevas columnas**: Generar columnas derivadas de otras, como calcular porcentajes o diferencias.
4. **Reorganizar datos**: Ordenar, agrupar o pivotar datos para facilitar el análisis.

## Transformaciones comunes

1. **Normalización**: Escalar los datos para que estén en un rango específico.
2. **Codificación**: Convertir datos categóricos en valores numéricos.
3. **Agrupación**: Agrupar datos por categorías y calcular estadísticas.
4. **Pivotar datos**: Transformar filas en columnas o viceversa.

## Importancia de las transformaciones

Las transformaciones de datos son esenciales para:

- **Preparar datos para modelos de aprendizaje automático**.
- **Reducir errores y mejorar la calidad de los datos**.
- **Facilitar el análisis y la visualización**.

<hr>

### Ahora que hemos entrado en contexto sobre qué son las transformaciones, vamos a ver como realizarlas. Para ello vamos a usar la biblioteca de **Pandas** y **Polars**

# ¿Qué es Pandas?

Pandas es una biblioteca de Python de código abierto que proporciona herramientas de análisis y manipulación de datos de alto rendimiento y fáciles de usar. Es ampliamente utilizada en el ámbito de la ciencia de datos, análisis estadístico y aprendizaje automático debido a su capacidad para manejar y procesar grandes volúmenes de datos de manera eficiente.

## ¿En qué se basa?

Pandas se basa en dos estructuras de datos principales:

- **Series**: Una estructura unidimensional similar a una lista o un array de NumPy, pero con etiquetas para los índices.
- **DataFrame**: Una estructura bidimensional similar a una tabla en una base de datos o una hoja de cálculo, con filas e índices etiquetados.

Estas estructuras permiten realizar operaciones complejas de análisis y manipulación de datos de manera sencilla.


## Funciones principales

Pandas incluye una amplia gama de funcionalidades, entre las que destacan:

- **Lectura y escritura de datos**: Importar y exportar datos desde/para múltiples formatos como CSV, Excel, JSON, SQL, y más.
- **Limpieza de datos**: Manejo de valores nulos, duplicados y transformación de datos.
- **Filtrado y selección**: Selección de filas y columnas basadas en condiciones.
- **Agrupación y agregación**: Agrupar datos y calcular estadísticas como suma, promedio, conteo, etc.
- **Manipulación de datos**: Ordenar, fusionar, concatenar y pivotar datos.
- **Análisis temporal**: Manejo de datos de series temporales, incluyendo fechas y frecuencias.

## ¿Para qué se usa Pandas?

Pandas es ideal para:

- **Análisis exploratorio de datos (EDA)**: Examinar y resumir datos para descubrir patrones y tendencias.
- **Preparación de datos**: Transformar datos en un formato adecuado para el análisis o modelado.
- **Análisis estadístico**: Calcular métricas y realizar operaciones estadísticas.
- **Integración con otras bibliotecas**: Trabajar junto con bibliotecas como NumPy y Matplotlib para análisis y visualización de datos.

## Mejores casos de uso

Pandas es especialmente útil en los siguientes escenarios:

1. **Análisis financiero**: Procesar datos de mercado y realizar cálculos financieros.
2. **Ciencia de datos**: Preparar conjuntos de datos para modelos de aprendizaje automático.
3. **Análisis de series temporales**: Trabajar con datos de tiempo como precios de acciones o datos meteorológicos.
4. **Limpieza de datos**: Transformar datos desordenados en un formato estructurado y limpio.
5. **Automatización de informes**: Generar informes basados en datos de manera programática.

## Instalación

Para instalar Pandas, puedes usar `pip`:

<details>
  <summary>Solución</summary>

```bash
pip install pandas
```

</details>

## Ejemplo básico

Vamos a realizar un ejemplo básico de cómo usar Pandas para cargar y filtrar datos de un archivo CSV:

<details>
  <summary>Solución: Cargamos los datos del archivo CSV ubicado en la carpeta de "Recursos"</summary>

```python
import pandas as pd

df = pd.read_csv('datos.csv')

# Mostramos el DataFrame
print(df)
```
</details>

<details>
  <summary>Solución: Filtramos los datos si el contenido de una columna en concreto es mayor a 25</summary>

```python
df_filtrado = df[df['columna'] > 25]

# Mostramos el DataFrame filtrado
print(df_filtrado)
```

</details>

## Ejemplo básico de transformación con Pandas

A continuación realizaremos un ejemplo paso a paso de cómo realizar transformaciones comunes con Pandas (Creación, Eliminación, Rellenado de valores nulos, Filtrado, Ordenación):

```python
import pandas as pd

# Creamos un DataFrame con datos de ejemplo y lo mostramos
data = {'Nombre': ['Ana', 'Luis', 'María', 'Juan'],
        'Edad': [25, 30, None, 22],
        'Salario': [3000, 4000, 3500, None]}

df = pd.DataFrame(data)

print(df)
```

<details>
  <summary>Solución: Eliminamos las edades con valores nulos (n/a)</summary>

```python
df_limpio = df['Edad'].dropna()

# Mostramos el DataFrame limpio
print(df_limpio)
```

</details>

<details>
  <summary>Solución: Rellenamos los valores nulos con un valor por defecto (0)</summary>

```python
df['Salario'] = df['Salario'].fillna(0)

# Mostramos el DataFrame con los valores nulos rellenados
print(df)
```
</details>

<details>
  <summary>Solución: Creamos una nueva columna "Salario_anual" cuyos valores son el resultado de multiplicar el valor correspondiente de la columna "Salario" por 12.</summary>

```python
df['Salario_anual'] = df['Salario'] * 12

# Mostramos el DataFrame con la nueva columna
print(df)
```

</details>


<details>
  <summary>Solución:  Filtramos los datos (solo personas mayores de 25 años)</summary>

```python
df_filtrado = df[df['Edad'] > 25]

# Mostramos el DataFrame filtrado
print(df_filtrado)
```

</details>

<details>
  <summary>Solución:  Ordenamos los datos por salario, podemos elegir si queremos orden ascendente (true) o como en este caso, descendente (False)</summary>

```python
df_ordenado = df.sort_values(by='Salario', ascending=False)

# Mostramos el DataFrame ordenado
print(df_ordenado)
```

</details>

## Recursos adicionales de Pandas

- [Documentación oficial de Pandas](https://pandas.pydata.org/docs/)
- [Repositorio de Pandas en GitHub](https://github.com/pandas-dev/pandas)
- [Tutoriales de Pandas en Python](https://pandas.pydata.org/docs/getting_started/index.html)
- [Guía de limpieza de datos con Pandas](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Transformaciones avanzadas con Pandas](https://pandas.pydata.org/docs/user_guide/reshaping.html)

<hr>

# ¿Qué es Polars?

Polars es una biblioteca de Python diseñada para el análisis y manipulación de datos, similar a Pandas, pero optimizada para un rendimiento más alto. Está escrita en Rust, lo que le permite ser extremadamente rápida y eficiente en el manejo de grandes volúmenes de datos. Polars es especialmente útil en escenarios donde el rendimiento y la escalabilidad son críticos.

## ¿En qué se basa?

Polars utiliza estructuras de datos optimizadas para el procesamiento de datos en memoria:

- **Series**: Una estructura unidimensional similar a las Series de Pandas, que representa una columna de datos.
- **DataFrame**: Una estructura bidimensional que organiza los datos en filas y columnas, diseñada para ser altamente eficiente en operaciones paralelas.

Estas estructuras están diseñadas para aprovechar al máximo los recursos del hardware, como la memoria y los núcleos de CPU.

## Funciones principales

Polars incluye una amplia gama de funcionalidades, entre las que destacan:

- **Lectura y escritura de datos**: Soporte para múltiples formatos como CSV, Parquet, JSON, y más.
- **Manipulación de datos**: Filtrado, selección, ordenación y agrupación de datos.
- **Operaciones en columnas**: Creación de nuevas columnas, transformación de datos y cálculos vectorizados.
- **Procesamiento en paralelo**: Aprovecha múltiples núcleos de CPU para acelerar las operaciones.
- **Soporte para datos de series temporales**: Manejo eficiente de datos con marcas de tiempo.

## ¿Para qué se usa Polars?

Polars es ideal para:

- **Procesamiento de grandes volúmenes de datos**: Manejo eficiente de datasets que no caben en memoria.
- **Análisis de datos de alto rendimiento**: Realizar operaciones complejas en grandes conjuntos de datos de manera rápida.
- **Procesamiento en pipelines**: Integración en flujos de trabajo de datos donde la velocidad es crucial.
- **Análisis de series temporales**: Trabajar con datos de tiempo de manera eficiente.

## Mejores casos de uso

Polars es especialmente útil en los siguientes escenarios:

1. **Big Data**: Procesar grandes volúmenes de datos que requieren un rendimiento superior.
2. **Análisis en tiempo real**: Realizar cálculos rápidos en datos que cambian constantemente.
3. **Procesamiento distribuido**: Integración con sistemas de procesamiento distribuido como Apache Arrow.
4. **Optimización de pipelines de datos**: Reducir el tiempo de ejecución en flujos de trabajo complejos.

## Instalación

Para instalar Polars, puedes usar `pip`:

<details>
  <summary>Solución</summary>

```bash
pip install polars
```

</details>

## Ejemplo básico

Vamos a realizar un ejemplo básico de cómo usar Polars para cargar y filtrar datos de un archivo CSV, observaréis que es muy similar al uso de Pandas:

<details>
  <summary>Solución: Cargamos los datos del archivo CSV ubicado en la carpeta de "Recursos"</summary>

```python
import polars as pl

df = pl.read_csv('datos.csv')

# Mostramos el DataFrame
print(df)
```

</details>

<details>
  <summary>Solución: Filtramos los datos si el contenido de una columna en concreto es mayor a 25</summary>

```python
df_filtrado = df.filter(pl.col('columna') > 25)

# Mostramos el DataFrame filtrado
print(df_filtrado)
```

</details>

## Ejemplo básico de transformación con Polars

A continuación realizaremos un ejemplo paso a paso de cómo realizar transformaciones comunes con Polars (Creación, Eliminación, Rellenado de valores nulos, Filtrado, Ordenación):

```python
import polars as pl

# Creamos un DataFrame con datos de ejemplo y lo mostramos
data = {'Nombre': ['Ana', 'Luis', 'María', 'Juan'],
        'Edad': [25, 30, None, 22],
        'Salario': [3000, 4000, 3500, None]}

df = pl.DataFrame(data)
```

<details>
  <summary>Solución: Eliminamos las filas con valores nulos</summary>

```python
df_limpio = df.drop_nulls()

# Mostramos el DataFrame limpio
print(df_limpio)
```
</details>

<details>
  <summary>Solución: Rellenamos los valores nulos con un valor por defecto (0)</summary>

```python
df = df.with_columns(pl.col('Salario').fill_null(0))

# Mostramos el DataFrame con los valores nulos rellenados
print(df)
```
</details>

<details>
  <summary>Solución: Creamos una nueva columna "Salario_anual" cuyos valores son el resultado de multiplicar el valor correspondiente de la columna "Salario" por 12</summary>

```python
df = df.with_columns((pl.col('Salario') * 12).alias('Salario_anual'))

# Mostramos el DataFrame con la nueva columna
print(df)
```
</details>

<details>
  <summary>Solución: Filtramos los datos (solo personas mayores de 25 años)</summary>

```python
df_filtrado = df.filter(pl.col('Edad') > 25)

# Mostramos el DataFrame filtrado
print(df_filtrado)
```
</details>

<details>
  <summary>Solución: Ordenamos los datos por salario en orden descendente</summary>

```python
df_ordenado = df.sort('Salario', reverse=True)

# Mostramos el DataFrame ordenado
print(df_ordenado)
```

</details>

## Recursos adicionales de Polars

- [Documentación oficial de Polars](https://pola.rs/)
- [Repositorio de Polars en GitHub](https://github.com/pola-rs/polars)
- [Tutoriales de Polars](https://pola.rs/book/)
- [Guía de optimización de datos con Polars](https://pola.rs/book/user-guide/)
- [Transformaciones avanzadas con Polars](https://pola.rs/book/user-guide/expressions/)


# Comparativa entre Pandas y Polars

| **Característica**        | **Pandas**                                   | **Polars**                                   |
|---------------------------|----------------------------------------------|----------------------------------------------|
| **Rendimiento**           | Bueno para datasets pequeños y medianos      | Excelente para grandes volúmenes de datos    |
| **Paralelismo**           | Limitado                                     | Soporte completo para procesamiento paralelo |
| **Manejo de memoria**     | Menos eficiente                              | Muy eficiente                                |
| **Facilidad de uso**      | Muy fácil, con una curva de aprendizaje baja | Fácil, pero requiere aprender nuevas APIs    |
| **Soporte para Big Data** | Limitado                                     | Excelente, compatible con Apache Arrow       |
| **Casos de uso ideales**  | Análisis exploratorio y preparación de datos | Procesamiento de datos a gran escala         |

## Resumen

- **Pandas** es ideal para tareas de análisis exploratorio y manipulación de datos en proyectos pequeños o medianos, gracias a su facilidad de uso y amplia documentación.
- **Polars** destaca en escenarios donde el rendimiento y la escalabilidad son críticos, siendo una opción excelente para trabajar con grandes volúmenes de datos o pipelines complejos.

<hr>

### ¡Bien! Ahora que hemos aprendido un poco sobre Pandas y Polars, vamos a ver la librería de NumPy, la cual será nuestra mayor aliada para la realización de operaciones matemáticas.

# ¿Qué es NumPy?

NumPy es una biblioteca fundamental para la computación científica en Python. Proporciona soporte para trabajar con arrays multidimensionales y una amplia colección de funciones matemáticas de alto rendimiento para operar con ellos. Es ampliamente utilizada en análisis de datos, aprendizaje automático, simulaciones científicas y más.

## ¿En qué se basa?

NumPy se basa en la estructura de datos llamada **ndarray** (array multidimensional), que permite realizar operaciones matemáticas de manera eficiente y vectorizada.

- **ndarray**: Una estructura de datos que representa un array multidimensional homogéneo (todos los elementos deben ser del mismo tipo).

Esta estructura está optimizada para realizar operaciones matemáticas y lógicas de manera rápida, aprovechando las capacidades del hardware.

## Funciones principales

NumPy incluye una amplia gama de funcionalidades, entre las que destacan:

- **Creación de arrays**: Generar arrays desde listas, rangos, o mediante funciones como `arange`, `linspace` y `random`.
- **Operaciones matemáticas**: Suma, resta, multiplicación, división, potencias, raíces, etc., aplicadas de manera vectorizada.
- **Manipulación de arrays**: Cambio de forma, transposición, concatenación y división de arrays.
- **Funciones estadísticas**: Cálculo de media, mediana, desviación estándar, varianza, etc.
- **Álgebra lineal**: Operaciones con matrices, determinantes, inversas, descomposiciones, etc.
- **Manejo de datos faltantes**: Uso de máscaras y valores especiales como `np.nan` (NaN = Not A Number).

## ¿Para qué se usa NumPy?

NumPy es ideal para:

- **Cálculos matemáticos y científicos**: Realizar operaciones complejas de manera eficiente.
- **Procesamiento de datos**: Manipular y transformar datos en arrays multidimensionales.
- **Simulaciones**: Crear modelos matemáticos y realizar simulaciones numéricas.
- **Aprendizaje automático**: Preparar datos para modelos de machine learning.
- **Gráficos y visualización**: Generar datos para visualizaciones con bibliotecas como Matplotlib.

## Mejores casos de uso

NumPy es especialmente útil en los siguientes escenarios:

1. **Procesamiento de imágenes**: Trabajar con datos de imágenes representados como arrays.
2. **Simulaciones científicas**: Resolver ecuaciones diferenciales, simulaciones físicas, etc.
3. **Análisis de datos**: Realizar cálculos estadísticos y transformaciones de datos.
4. **Optimización matemática**: Resolver problemas de optimización y álgebra lineal.
5. **Preparación de datos**: Transformar datos en un formato adecuado para modelos de aprendizaje automático.

## Instalación

Para instalar NumPy, puedes usar `pip`:

<details>
  <summary>Solución</summary>

```bash
pip install numpy
```
</details>

## Ejemplo básico de cómo usar NumPy para crear y manipular arrays:

Vamos a realizar un ejemplo básico de cómo usar NumPy para crear y manipular arrays:


<details> 
  <summary>Solución: Creamos un array unidimensional(array) y otro bidimensional(matriz)</summary>

```python
import numpy as np

array = np.array([1, 2, 3, 4, 5])
matriz = np.array([[1, 2, 3], [4, 5, 6]])

# Mostramos el array y la matriz
print("Array unidimensional:", array)
print("Matriz bidimensional:\n", matriz)
```

</details>

<details> 
  <summary>Solución:  Realizamos operaciones matemáticas (Array multiplicado por 2, Suma de los elementos de la matriz)</summary>

```python
array_doble = array * 2
suma = np.sum(matriz)

# Mostramos los resultados
print("Array multiplicado por 2:", array_doble)
print("Suma de los elementos de la matriz:", suma)
```

</details>


## Ejemplo básico de transformación con NumPy

<details> 
  <summary>Solución: Creamos un array con valores aleatorios</summary>

```python
import numpy as np

array = np.random.randint(1, 100, size=(4, 4))

# Mostramos el array
print("Array:\n", array)
```
</details>

<details> 
  <summary>Solución: Calculamos la media y la desviación estándar</summary>

```python
media = np.mean(array)
desviacion = np.std(array)

print("Media:", media)
print("Desviación estándar:", desviacion)
```

</details>

<details> 
  <summary>Solución: Normalizamos los datos (restamos la media y dividimos por la desviación estándar)</summary>

```python
array_normalizado = (array - media) / desviacion

print("Array normalizado:\n", array_normalizado)
```
</details>

<details> 
  <summary>Solución: Transponemos el array</summary>

```python
array_transpuesto = array.T

print("Array transpuesto:\n", array_transpuesto)
```
</details>

<details> 
  <summary>Solución: Filtramos los elementos del array inicial mayores a 50</summary>

```python
array_filtrado = array[array > 50]

print("Elementos mayores a 50:", array_filtrado)
```

</details>

## Recursos adicionales de NumPy

- [Documentación oficial de NumPy](https://numpy.org/doc/)
- [Repositorio de NumPy en GitHub](https://github.com/numpy/numpy)
- [Tutoriales de NumPy](https://numpy.org/doc/stable/user/quickstart.html)
- [Funciones estadísticas en NumPy](https://numpy.org/doc/stable/reference/routines.statistics.html)

<hr>