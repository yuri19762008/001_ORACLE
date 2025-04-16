import pandas as pd
import matplotlib.pyplot as plt

# Nombres de archivos y tiendas
archivos = [
    "tiendas/tienda_1.csv",
    "tiendas/tienda_2.csv",
    "tiendas/tienda_3.csv",
    "tiendas/tienda_4.csv"
]
nombres_tiendas = ["Tienda 1", "Tienda 2", "Tienda 3", "Tienda 4"]

# 1. Gráfico de barras: Ingresos totales por tienda
ingresos = []
for archivo in archivos:
    df = pd.read_csv(archivo)
    ingresos.append(df['Precio'].sum())

plt.figure(figsize=(10,6))
plt.bar(nombres_tiendas, ingresos, color=["blue", "orange", "green", "red"])
plt.title("Ingresos Totales por Tienda")
plt.xlabel("Tiendas")
plt.ylabel("Ingresos Totales")
plt.tight_layout()
plt.savefig("ingresos_tiendas.png")
plt.show()

# 2. Gráfico circular: Categoría más vendida por tienda
categorias = []
for archivo in archivos:
    df = pd.read_csv(archivo)
    categorias.append(df['Categoría del Producto'].mode()[0])

cat_counts = pd.Series(categorias).value_counts()
plt.figure(figsize=(8,8))
plt.pie(cat_counts, labels=cat_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Categoría Más Vendida por Tienda")
plt.tight_layout()
plt.savefig("categoria_mas_vendida.png")
plt.show()

# 3. Gráfico de caja: Distribución de calificaciones por tienda
calificaciones = []
for archivo in archivos:
    df = pd.read_csv(archivo)
    calificaciones.append(df['Calificación'])

plt.figure(figsize=(10,6))
plt.boxplot(calificaciones, labels=nombres_tiendas)
plt.title("Distribución de Calificaciones por Tienda")
plt.xlabel("Tiendas")
plt.ylabel("Calificación")
plt.tight_layout()
plt.savefig("calificaciones_boxplot.png")
plt.show()
