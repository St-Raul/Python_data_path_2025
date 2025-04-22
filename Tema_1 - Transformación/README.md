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
2. **Codificación**: Convertir datos categóricos en valores numéricos (por ejemplo, con `pd.get_dummies`).
3. **Agrupación**: Agrupar datos por categorías y calcular estadísticas.
4. **Pivotar datos**: Transformar filas en columnas o viceversa.

## Importancia de las transformaciones

Las transformaciones de datos son esenciales para:

- **Preparar datos para modelos de aprendizaje automático**.
- **Reducir errores y mejorar la calidad de los datos**.
- **Facilitar el análisis y la visualización**.


# PANDAS, ¿qué es Pandas?

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

```bash
pip install pandas
```

## Ejemplo básico

Vamos a realizar un ejemplo básico de cómo usar Pandas para cargar y filtrar datos de un archivo CSV:

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

## Ejemplo básico de transformación con Pandas

A continuación realizaremos un ejemplo paso a paso de cómo realizar transformaciones comunes con Pandas (Creación, Eliminación,Rellenado de valores nulos(modificación), Filtrado, Ordenación):

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

## Recursos adicionales

- [Documentación oficial de Pandas](https://pandas.pydata.org/docs/)
- [Repositorio de Pandas en GitHub](https://github.com/pandas-dev/pandas)
- [Tutoriales de Pandas en Python](https://pandas.pydata.org/docs/getting_started/index.html)
- [Guía de limpieza de datos con Pandas](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Transformaciones avanzadas con Pandas](https://pandas.pydata.org/docs/user_guide/reshaping.html)
