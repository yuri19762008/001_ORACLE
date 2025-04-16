### Análisis de Desempeño de Tiendas - Alura Store


Este proyecto utiliza Python y librerías como pandas y matplotlib para analizar y visualizar datos de ventas, productos, reseñas y logística de las 4 tiendas de la cadena Alura Store. El objetivo es identificar la tienda menos eficiente y presentar recomendaciones basadas en datos para la toma de decisiones estratégicas.

# Funcionalidades principales
    Carga de datos desde URLs:
    Los archivos CSV de las tiendas se leen directamente desde enlaces públicos de GitHub, facilitando la portabilidad y actualización de los datos.

# Análisis de facturación:
    Se calcula el ingreso total, cantidad de ventas, precio promedio, máximo y mínimo por tienda.

# Ventas por categorías:
    Se suman las ventas totales por cada categoría de producto, tanto de forma global como desglosadas por tienda.

# Calificación promedio:
    Se obtiene la calificación promedio de los clientes para cada tienda, permitiendo comparar la satisfacción del cliente entre sucursales.

# Productos más y menos vendidos:
    Se identifican los productos con mayor y menor cantidad de ventas en cada tienda.

# Costo de envío promedio:
    Se calcula el costo de envío promedio para cada tienda, útil para evaluar la competitividad logística.

# Visualizaciones automáticas:
    El proyecto genera gráficos de barras, gráficos de torta (pie charts) y boxplots para comparar ingresos, categorías, calificaciones y más, tanto de forma global como por tienda.

# Exportación de resultados:
    Los análisis y gráficos pueden exportarse a archivos Excel profesionales, incluyendo la inserción automática de gráficos en las hojas correspondientes.

# Recomendación final:
    Basado en los indicadores clave (ingresos, calificaciones, logística), el sistema recomienda cuál tienda es la mejor candidata para ser vendida.

# Estructura del proyecto
    Carga y análisis de datos:
    Scripts en Python para análisis por tienda y por categoría.

# Visualizaciones:
    Gráficos generados automáticamente y guardados en carpetas específicas.

# Exportación a Excel:
    Resultados y gráficos integrados en archivos Excel para reportes ejecutivos.

# Recomendación:
    Texto y archivo con la sugerencia de acción basada en los datos.

### Instalación de dependencias con requirements.txt
    Para que cualquier persona pueda ejecutar el proyecto sin problemas, incluye el archivo requirements.txt en el repositorio. Este archivo contiene la lista de todas las librerías de Python necesarias.

# Pasos para instalar dependencias
    Abre una terminal en la carpeta raíz del proyecto.

# Ejecuta el siguiente comando para instalar todas las librerías necesarias:

        pip install -r requirements.txt