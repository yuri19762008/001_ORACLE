import pandas as pd
import matplotlib.pyplot as plt
import os

# Asegúrate de que la carpeta exista
os.makedirs("categorias", exist_ok=True)

# URLs de los archivos CSV
urls = [
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv",
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv",
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv",
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"
]
nombres_tiendas = ["Tienda 1", "Tienda 2", "Tienda 3", "Tienda 4"]

# Categorías a mostrar
categorias_analizar = [
    "Electrónicos", "Muebles", "Juguetes", "Electrodomésticos",
    "Artículos para el hogar", "Deportes y diversión", "Libros", "Instrumentos musicales"
]

for url, nombre in zip(urls, nombres_tiendas):
    df = pd.read_csv(url)
    conteo = df['Categoría del Producto'].value_counts().reindex(categorias_analizar, fill_value=0)
    plt.figure(figsize=(7,7))
    plt.pie(conteo, labels=conteo.index, autopct='%1.1f%%', startangle=140)
    plt.title(f"Distribución de categorías en {nombre}")
    plt.tight_layout()
    plt.savefig(f"categorias/torta_categorias_{nombre.replace(' ', '_').lower()}.png")
    plt.close()
