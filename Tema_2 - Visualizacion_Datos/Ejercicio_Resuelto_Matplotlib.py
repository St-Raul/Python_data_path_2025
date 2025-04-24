import os
import polars as pl
import numpy as np
import matplotlib.pyplot as plt

# Verificar si el archivo existe
if os.path.exists('Netflix_Dataset.csv'):
    # Cargar el archivo Netflix_Dataset.csv utilizando Polars
    df = pl.read_csv('Netflix_Dataset.csv')
    print("Archivo cargado exitosamente.")
else:
    raise FileNotFoundError("El archivo 'Netflix_Dataset.csv' no se encuentra en la carpeta actual.")

# Filtrar las columnas relevantes
columnas_relevantes = ['Title', 'Genre', 'IMDb Score', 'Rotten Tomatoes Score', 'Metacritic Score', 'Runtime', 'Release Date', 'Netflix Release Date', 'Series or Movie']
df = df.select(columnas_relevantes)

# Limpieza de datos
# 1. Rellenar valores nulos en columnas numéricas con la media
columnas_numericas = ['IMDb Score', 'Rotten Tomatoes Score', 'Metacritic Score']
for columna in columnas_numericas:
    media = df[columna].mean()
    df = df.with_columns(
        pl.col(columna).fill_null(media)
    )

# 2. Rellenar valores nulos en columnas categóricas con "Unknown"
df = df.with_columns(
    pl.col('Genre').fill_null('Unknown')
)

# 3. Convertir columnas de fechas al formato de fecha de Polars
columnas_fechas = ['Release Date', 'Netflix Release Date']
for columna in columnas_fechas:
    df = df.with_columns(
        pl.col(columna).str.strptime(pl.Date, format="%Y-%m-%d", strict=False)
    )

# 4. Estandarizar la columna Runtime a minutos
# Paso 1: Quitar los símbolos ">" y "<"
df = df.with_columns(
    pl.col('Runtime').str.replace_all(r'[><]', '').str.strip_chars()
)

# Paso 2: Procesar valores en minutos (que contienen "minutes" o "mins")
df = df.with_columns(
    pl.when(pl.col('Runtime').str.contains(r'\b(minutes|mins)\b'))
    .then(pl.col('Runtime').str.extract(r'(\d+)', 1).cast(pl.Int32))
    .otherwise(pl.col('Runtime'))
    .alias('Runtime')
)

# Paso 3: Procesar valores en horas (que contienen "hour", "hrs" o rangos como "1-2 hour")
df = df.with_columns(
    pl.when(pl.col('Runtime').str.contains(r'\b(hour|hrs)\b'))
    .then(
        pl.when(pl.col('Runtime').str.contains(r'-'))  # Si es un rango como "1-2 hour"
        .then(
            (
                pl.col('Runtime')
                .str.extract(r'(\d+)-?(\d+)?', 1)  # Extraer el primer número
                .cast(pl.Float64)
                .add(
                    pl.col('Runtime')
                    .str.extract(r'(\d+)-?(\d+)?', 2)  # Extraer el segundo número (si existe)
                    .cast(pl.Float64)
                    .fill_null(0)
                )
                / 2  # Calcular la media si hay dos números
                * 60  # Convertir a minutos
            )
        )
        .otherwise(  # Si no es un rango, como "2 hrs"
            pl.col('Runtime')
            .str.extract(r'(\d+)', 1)  # Extraer el número
            .cast(pl.Float64)
            * 60  # Convertir a minutos
        )
        .cast(pl.Int32)
    )
    .otherwise(pl.col('Runtime'))
    .alias('Runtime')
)

# Convertir la columna Runtime a tipo Int32 para asegurar consistencia
df = df.with_columns(
    pl.col('Runtime').cast(pl.Int32, strict=False)
)

# Sustituir valores nulos en la columna Runtime por 0
df = df.with_columns(
    pl.col('Runtime').fill_null(0)
)

# Normalizar Rotten Tomatoes Score a una escala de 0 a 10
df = df.with_columns(
    (pl.col("Rotten Tomatoes Score") / 10).alias("Rotten Tomatoes Score Normalizado")
)

### Parte 1: Promedio de Puntuaciones por Género ###
# Análisis: Calcular el promedio de puntuaciones por género
promedio_puntuaciones = (
    df.group_by("Genre")
    .agg([
        pl.col("IMDb Score").mean().alias("Promedio IMDb"),
        pl.col("Rotten Tomatoes Score Normalizado").mean().alias("Promedio Rotten Tomatoes"),
        pl.len().alias("Cantidad")
    ])
    .sort("Cantidad", descending=True)
    .head(10)  # Seleccionar los 10 géneros más populares
)

# Visualización: Gráfico de barras
plt.figure(figsize=(10, 6))
x = promedio_puntuaciones["Genre"]
y_imdb = promedio_puntuaciones["Promedio IMDb"]
y_rotten = promedio_puntuaciones["Promedio Rotten Tomatoes"]

bar_width = 0.35
index = range(len(x))

plt.bar(index, y_imdb, bar_width, label="Promedio IMDb", color="blue")
plt.bar([i + bar_width for i in index], y_rotten, bar_width, label="Promedio Rotten Tomatoes", color="orange")

plt.xlabel("Género")
plt.ylabel("Puntuación Promedio (Escala 0-10)")
# Ajustar los límites del eje para mejor visualización, escogiendo el menor y el mayor de ambos
plt.ylim(min(min(y_imdb.to_list()), min(y_rotten.to_list())) - 1, max(max(y_imdb.to_list()), max(y_rotten.to_list())) + 1)
plt.title("Promedio de Puntuaciones por Género (Top 10)")
plt.xticks([i + bar_width / 2 for i in index], x, rotation=45, ha="right")
plt.legend()
plt.tight_layout()

# Mostrar el gráfico
plt.show()

### Parte 2: Relación entre Puntuaciones ###
# Análisis: Extraer las columnas necesarias
imdb_scores = df["IMDb Score"].to_list()
rotten_scores = df["Rotten Tomatoes Score Normalizado"].to_list()

# Visualización: Gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(imdb_scores, rotten_scores, alpha=0.6, color="purple", label="Puntuaciones")

# Ajustar etiquetas y título
plt.xlabel("IMDb Score (Escala 0-10)")
plt.ylabel("Rotten Tomatoes Score (Escala 0-10)")
plt.title("Relación entre IMDb Score y Rotten Tomatoes Score")

# Calcular y trazar la línea de tendencia
z = np.polyfit(imdb_scores, rotten_scores, 1)  # Ajuste lineal
p = np.poly1d(z)
plt.plot(imdb_scores, p(imdb_scores), color="red", label="Línea de tendencia")

# Mostrar leyenda y gráfico
plt.legend()
plt.tight_layout()
plt.show()

### Parte 3: Distribución de Puntuaciones de IMDb ###
# Análisis: Calcular estadísticas de la distribución
imdb_scores = np.array(df["IMDb Score"].to_list())
media = np.mean(imdb_scores)
mediana = np.median(imdb_scores)
desviacion_estandar = np.std(imdb_scores)

print(f"Media: {media:.2f}, Mediana: {mediana:.2f}, Desviación Estándar: {desviacion_estandar:.2f}")

# Visualización: Histograma
plt.figure(figsize=(10, 6))
plt.hist(imdb_scores, bins=10, color="skyblue", edgecolor="black", alpha=0.7)

# Añadir líneas para la media y la mediana
plt.axvline(media, color="red", linestyle="dashed", linewidth=1, label=f"Media: {media:.2f}")
plt.axvline(mediana, color="green", linestyle="dashed", linewidth=1, label=f"Mediana: {mediana:.2f}")

# Ajustar etiquetas y título
plt.xlabel("IMDb Score (Escala 0-10)")
plt.ylabel("Frecuencia")
plt.title("Distribución de Puntuaciones de IMDb")
plt.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.show()

### Parte 4: Análisis Temporal ###
# Análisis: Agrupar por año de lanzamiento y tipo
df = df.with_columns(
    pl.col("Release Date").dt.year().alias("Release Year")  # Extraer el año de la fecha de lanzamiento
)

# Agrupar por año y tipo (Series o Película)
temporal_data = (
    df.group_by(["Release Year", "Series or Movie"])
    .agg(pl.len().alias("Cantidad"))
    .sort("Release Year")
)

# Separar los datos por tipo
movies_data = temporal_data.filter(pl.col("Series or Movie") == "Movie")
series_data = temporal_data.filter(pl.col("Series or Movie") == "Series")

# Visualización: Gráfico de líneas
plt.figure(figsize=(12, 6))

# Línea para películas
plt.plot(
    movies_data["Release Year"],
    movies_data["Cantidad"],
    label="Películas",
    marker="o",
    color="blue"
)

# Línea para series
plt.plot(
    series_data["Release Year"],
    series_data["Cantidad"],
    label="Series",
    marker="o",
    color="orange"
)

# Ajustar etiquetas y título
plt.xlabel("Año de Lanzamiento")
plt.ylabel("Cantidad")
plt.title("Evolución del Número de Películas y Series por Año")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Exportación de Gráficos
# Guardar el gráfico de promedio de puntuaciones por género
plt.figure(figsize=(10, 6))
plt.bar(index, y_imdb, bar_width, label="Promedio IMDb", color="blue")
plt.bar([i + bar_width for i in index], y_rotten, bar_width, label="Promedio Rotten Tomatoes", color="orange")
plt.xlabel("Género")
plt.ylabel("Puntuación Promedio (Escala 0-10)")
plt.title("Promedio de Puntuaciones por Género (Top 10)")
plt.xticks([i + bar_width / 2 for i in index], x, rotation=45, ha="right")
plt.legend()
plt.tight_layout()
plt.savefig("promedio_puntuaciones_por_genero.png")
plt.close()

# Guardar el gráfico de relación entre puntuaciones
plt.figure(figsize=(10, 6))
plt.scatter(imdb_scores, rotten_scores, alpha=0.6, color="purple", label="Puntuaciones")
plt.plot(imdb_scores, p(imdb_scores), color="red", label="Línea de tendencia")
plt.xlabel("IMDb Score (Escala 0-10)")
plt.ylabel("Rotten Tomatoes Score (Escala 0-10)")
plt.title("Relación entre IMDb Score y Rotten Tomatoes Score")
plt.legend()
plt.tight_layout()
plt.savefig("relacion_puntuaciones.png")
plt.close()

# Guardar el histograma de distribución de IMDb
plt.figure(figsize=(10, 6))
plt.hist(imdb_scores, bins=10, color="skyblue", edgecolor="black", alpha=0.7)
plt.axvline(media, color="red", linestyle="dashed", linewidth=1, label=f"Media: {media:.2f}")
plt.axvline(mediana, color="green", linestyle="dashed", linewidth=1, label=f"Mediana: {mediana:.2f}")
plt.xlabel("IMDb Score (Escala 0-10)")
plt.ylabel("Frecuencia")
plt.title("Distribución de Puntuaciones de IMDb")
plt.legend()
plt.tight_layout()
plt.savefig("distribucion_imdb.png")
plt.close()

# Guardar el gráfico de evolución temporal
plt.figure(figsize=(12, 6))
plt.plot(movies_data["Release Year"], movies_data["Cantidad"], label="Películas", marker="o", color="blue")
plt.plot(series_data["Release Year"], series_data["Cantidad"], label="Series", marker="o", color="orange")
plt.xlabel("Año de Lanzamiento")
plt.ylabel("Cantidad")
plt.title("Evolución del Número de Películas y Series por Año")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("evolucion_temporal.png")
plt.close()

# Exportación de Datos Procesados
# Seleccionar 20 registros aleatorios del dataset final
df_sample = df.sample(n=20, with_replacement=False)

# Guardar los registros seleccionados en un archivo CSV
df_sample.write_csv("Netflix_Dataset_Procesado_Muestra.csv")

