import polars as pl
import numpy as np
import json
import os

### PRIMER PUNTO ###

## Cargar el archivo Netflix_Dataset.csv utilizando Polars ##
# - Se utiliza pl.read_csv para cargar el archivo CSV en un DataFrame de Polars.
# - Se verifica si el archivo existe en la carpeta actual antes de cargarlo.
if os.path.exists('Netflix_Dataset.csv'):
    df = pl.read_csv('Netflix_Dataset.csv')
else:
    raise FileNotFoundError("El archivo 'Netflix_Dataset.csv' no se encuentra en la carpeta actual.")

## Verificar valores nulos y calcular el porcentaje de valores faltantes por columna ##
# - Se utiliza df.null_count() para contar los valores nulos por columna.
# - Se calcula el porcentaje de valores faltantes dividiendo los valores nulos entre el total de filas.
num_valores_nulos_colum = df.null_count()
porcentaje_faltante = (num_valores_nulos_colum / df.shape[0]) * 100
print("Porcentaje de valores faltantes por columna:")
print(porcentaje_faltante, "\n")

## Identificar columnas categóricas y numéricas ##
# - Las columnas categóricas se identifican como aquellas con tipo Utf8 (strings).
# - Las columnas numéricas se identifican como aquellas con tipo Float64 o Int64.
columnas_categoricas = [col for col, dtype in zip(df.columns, df.dtypes) if dtype == pl.Utf8]
columnas_numericas = [col for col, dtype in zip(df.columns, df.dtypes) if dtype in [pl.Float64, pl.Int64]]

print("Columnas categóricas:")
print(columnas_categoricas, "\n")

print("Columnas numéricas:")
print(columnas_numericas, "\n")

### SEGUNDO PUNTO ###

## Rellenar valores nulos en columnas numéricas con la media de cada columna ##
# - Se calcula la media de cada columna numérica con df[col].mean().
# - Se utiliza fill_null para reemplazar los valores nulos con la media.
for col in columnas_numericas:
    media_colum = df[col].mean()
    df = df.with_columns(
        pl.col(col).fill_null(media_colum).alias(col)
    )

## Rellenar valores nulos en columnas categóricas con la moda (valor más frecuente) ##
# - Se utiliza df[col].drop_nulls() antes de calcular la moda para asegurarse de que no se incluyan valores nulos en el cálculo.
# - Se verifica que mode_value no sea None y que tenga al menos un elemento antes de intentar acceder a mode_value[0].
# - Nos aseguramos de que el valor de mode_value[0] sea compatible con el tipo de datos de la columna.
for col in columnas_categoricas:
    moda_colum = df[col].drop_nulls().mode()
    if moda_colum is not None and len(moda_colum) > 0:
        moda_colum = moda_colum[0]  # Nos aseguramos de obtener el valor correcto
        df = df.with_columns(
            pl.col(col).fill_null(moda_colum).alias(col)
        )
    else:
        print(f"No se pudo calcular la moda para la columna: {col}")

## Convertir columnas de fechas al formato de fecha de Polars ##
columnas_fecha = ["Release Date", "Netflix Release Date"]
for col in columnas_fecha:
    if col in df.columns:
        df = df.with_columns(
            pl.col(col).str.strptime(pl.Date, format="%Y-%m-%d", strict=False).alias(col)
        )

## Verificar que no queden valores nulos ##
print("Valores nulos después de la limpieza:")
print(df.null_count(), "\n")

### TERCER PUNTO ###

## Película con la mayor puntuación de IMDb ##
# - Se filtra el dataset para encontrar la fila con el valor máximo en la columna IMDb Score.
# - Se utiliza df["IMDb Score"].max() para obtener el valor máximo de la columna IMDb Score.
# - Puede darse el caso de que haya varias películas con la misma puntuación máxima.
pelicula_max_imdb = df.filter(pl.col("IMDb Score") == df["IMDb Score"].max())
print("Película con la mayor puntuación de IMDb:")
print(pelicula_max_imdb.select(["Title", "IMDb Score"]), "\n")

## Película con la mayor puntuación de Rotten Tomatoes ##
# - Similar al caso anterior, pero se utiliza la columna Rotten Tomatoes Score.
# - Al igual que el anterior, puede darse el caso de que haya varias películas con la misma puntuación máxima.
pelicula_max_rotten = df.filter(pl.col("Rotten Tomatoes Score") == df["Rotten Tomatoes Score"].max())
print("Película con la mayor puntuación de Rotten Tomatoes:")
print(pelicula_max_rotten.select(["Title", "Rotten Tomatoes Score"]), "\n")

## País con mayor disponibilidad de contenido ##
# - Se utiliza str.split(",") para dividir los países en una lista.
# - Se usa explode para expandir las listas en filas individuales.
# - Se agrupan los datos por país y se cuenta la cantidad de ocurrencias.
pais_mayor_disponibilidad = (
    df.select(pl.col("Country Availability").str.split(","))
    .explode("Country Availability")
    .group_by("Country Availability")
    .len()
    .sort("len", descending=True)
    .head(1)  # Solo obtenemos el país con mayor disponibilidad
)
print("País con mayor disponibilidad de contenido:")
print(pais_mayor_disponibilidad, "\n")

## Agrupar por género y calcular el promedio de las puntuaciones ##
# - Se agrupan los datos por la columna Genre.
# - Se calculan los promedios de las columnas IMDb Score, Rotten Tomatoes Score y Metacritic Score.
promedio_puntuaciones_por_genero = (
    df.group_by("Genre")
    .agg([
        pl.col("IMDb Score").mean().alias("Promedio IMDb"),
        pl.col("Rotten Tomatoes Score").mean().alias("Promedio Rotten Tomatoes"),
        pl.col("Metacritic Score").mean().alias("Promedio Metacritic")
    ])
    .sort("Promedio IMDb", descending=True)
)
print("Promedio de puntuaciones por género:")
print(promedio_puntuaciones_por_genero, "\n")

## Número de películas y series disponibles ##
# - Se agrupan los datos por la columna Series or Movie y se cuenta la cantidad de filas en cada grupo.
conteo_peliculas_series = df.group_by("Series or Movie").len()
print("Número de películas y series disponibles:")
print(conteo_peliculas_series, "\n")


### CUARTO PUNTO ###

## Convertir las columnas de puntuaciones a arrays de NumPy ##
# - Se convierten las columnas IMDb Score, Rotten Tomatoes Score y Metacritic Score a arrays de NumPy utilizando to_numpy().
imdb_puntuaciones = df["IMDb Score"].to_numpy()
rotten_puntuaciones = df["Rotten Tomatoes Score"].to_numpy()
metacritic_puntuaciones = df["Metacritic Score"].to_numpy()

## Calcular la correlación entre las puntuaciones ##
# - Se utiliza np.corrcoef para calcular la matriz de correlación entre las puntuaciones.
matriz_correlacion = np.corrcoef([imdb_puntuaciones, rotten_puntuaciones, metacritic_puntuaciones])
print("Matriz de correlación entre las puntuaciones:")
print(matriz_correlacion, "\n")

## Calcular la desviación estándar de las puntuaciones ##
# - Se utiliza np.std con ddof=1 (grados de libertad) para calcular la desviación estándar de cada conjunto de puntuaciones.
std_imdb = np.std(imdb_puntuaciones, ddof=1)
std_rotten = np.std(rotten_puntuaciones, ddof=1)
std_metacritic = np.std(metacritic_puntuaciones, ddof=1)

print("Desviación estándar de las puntuaciones:")
print(f"IMDb Score: {std_imdb}")
print(f"Rotten Tomatoes Score: {std_rotten}")
print(f"Metacritic Score: {std_metacritic}", "\n")


### QUINTO PUNTO ###

## Calcular el Overall Score como promedio ponderado de las puntuaciones ##
# - Se calcula como un promedio ponderado de las puntuaciones:
#       IMDb Score: 50%
#       Rotten Tomatoes Score: 30%
#       Metacritic Score: 20%
# - Se agrega como una nueva columna al DataFrame.

df = df.with_columns(
    (
        (pl.col("IMDb Score") * 0.5) +
        (pl.col("Rotten Tomatoes Score") * 0.3) +
        (pl.col("Metacritic Score") * 0.2)
    ).alias("Overall Score")
)

## Guardar el DataFrame actualizado en un nuevo archivo CSV ##
# - Se guarda el DataFrame actualizado con la nueva columna Overall Score en un archivo llamado Netflix_Dataset_with_Overall_Score.csv.
df.write_csv("Netflix_Dataset_with_Overall_Score.csv")
print("Archivo CSV guardado como 'Netflix_Dataset_with_Overall_Score.csv'.")

## Crear un resumen con las estadísticas clave ##
# - Se recopilan las estadísticas clave calculadas previamente en un diccionario.
# - Se convierte la matriz de correlación a una lista con .tolist() para que sea serializable en JSON.
resumen_estadisticas = {
    "pelicula_max_imdb": pelicula_max_imdb.select(["Title", "IMDb Score"]).to_dict(as_series=False),
    "pelicula_max_rotten": pelicula_max_rotten.select(["Title", "Rotten Tomatoes Score"]).to_dict(as_series=False),
    "pais_mayor_disponibilidad": pais_mayor_disponibilidad.to_dict(as_series=False),
    "promedio_puntuaciones_por_genero": promedio_puntuaciones_por_genero.to_dict(as_series=False),
    "conteo_peliculas_series": conteo_peliculas_series.to_dict(as_series=False),
    "desviacion_estandar": {
        "IMDb Score": std_imdb,
        "Rotten Tomatoes Score": std_rotten,
        "Metacritic Score": std_metacritic
    },
    "correlacion_puntuaciones": matriz_correlacion.tolist()
}

## Guardar el resumen en un archivo JSON ##
# - Se guarda el resumen en un archivo JSON llamado Resumen_Estadisticas.json.
with open("Resumen_Estadisticas.json", "w", encoding="utf-8") as json_file:
    json.dump(resumen_estadisticas, json_file, indent=4, ensure_ascii=False)
print("Resumen guardado como 'Resumen_Estadisticas.json'.")
