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
  <summary>Solución</summary>
        ```python
        import pandas as pd

        # Cargamos los datos de un archivo CSV
        df = pd.read_csv('datos.csv')

        # Mostramos el DataFrame
        print(df)

        # Filtramos los datos si el contenido de una columna en concreto es mayor a 10
        df_filtrado = df[df['columna'] > 10]
        print(df_filtrado)
        ```
</details>


## Ejemplo básico de transformación con Pandas

A continuación realizaremos un ejemplo paso a paso de cómo realizar transformaciones comunes con Pandas (Creación, Eliminación,Rellenado de valores nulos(modificación), Filtrado, Ordenación):

<details>
 <summary>Solución</summary>
        ```python
        import pandas as pd

        # Creamos un DataFrame con datos de ejemplo 
        data = {'Nombre': ['Ana', 'Luis', 'María', 'Juan'],
                'Edad': [25, 30, None, 22],
                'Salario': [3000, 4000, 3500, None]}

        df = pd.DataFrame(data)

        # Eliminamos las filas con valores nulos (n/a) 
        df_limpio = df.dropna()

        # Rellenamos los valores nulos con un valor por defecto (0) 
        df['Salario'] = df['Salario'].fillna(0)

        # Creamos una nueva columna "Salario_anual" cuyos valores son el resultado de multiplicar el valor correspondiente de la columna "Salario" por 12. 
        df['Salario_anual'] = df['Salario'] * 12

        # Filtramos los datos (solo personas mayores de 25 años) 
        df_filtrado = df[df['Edad'] > 25]

        # Ordenamos los datos por salario, podemos elegir si queremos orden ascendente (true) o como en este caso, descendente (False) 
        df_ordenado = df.sort_values(by='Salario', ascending=False)

        print(df_ordenado)
        ```
</details>

## Recursos adicionales de Pandas

- [Documentación oficial de Pandas](https://pandas.pydata.org/docs/)
- [Repositorio de Pandas en GitHub](https://github.com/pandas-dev/pandas)
- [Tutoriales de Pandas en Python](https://pandas.pydata.org/docs/getting_started/index.html)
- [Guía de limpieza de datos con Pandas](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Transformaciones avanzadas con Pandas](https://pandas.pydata.org/docs/user_guide/reshaping.html)


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
  <summary>Solución</summary>
        ```python
        import polars as pl

        # Cargamos los datos de un archivo CSV
        df = pl.read_csv('datos.csv')

        # Mostramos el DataFrame
        print(df)

        # Filtramos los datos si el contenido de una columna en concreto es mayor a 10
        df_filtrado = df.filter(pl.col('columna') > 10)
        print(df_filtrado)
        ```
</details>

## Ejemplo básico de transformación con Pandas

A continuación realizaremos un ejemplo paso a paso de cómo realizar transformaciones comunes con Polars (Creación, Eliminación, Rellenado de valores nulos, Filtrado, Ordenación):

<details>
  <summary>Solución</summary>
        ```python
        import polars as pl

        # Creamos un DataFrame con datos de ejemplo
        data = {'Nombre': ['Ana', 'Luis', 'María', 'Juan'],
                'Edad': [25, 30, None, 22],
                'Salario': [3000, 4000, 3500, None]}

        df = pl.DataFrame(data)

        # Eliminamos las filas con valores nulos
        df_limpio = df.drop_nulls()

        # Rellenamos los valores nulos con un valor por defecto (0)
        df = df.with_columns(pl.col('Salario').fill_null(0))

        # Creamos una nueva columna "Salario_anual" cuyos valores son el resultado de multiplicar el valor correspondiente de la columna "Salario" por 12
        df = df.with_columns((pl.col('Salario') * 12).alias('Salario_anual'))

        # Filtramos los datos (solo personas mayores de 25 años)
        df_filtrado = df.filter(pl.col('Edad') > 25)

        # Ordenamos los datos por salario en orden descendente
        df_ordenado = df.sort('Salario', reverse=True)

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