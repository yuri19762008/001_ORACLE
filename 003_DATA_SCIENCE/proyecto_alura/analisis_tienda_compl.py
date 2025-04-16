import pandas as pd
import matplotlib.pyplot as plt
import os
import traceback
from typing import Dict, List, Optional

class AnalisisTienda:
    def __init__(self, directorio_datos="tiendas/"):
        """Inicialización con el directorio donde están los archivos CSV"""
        self.directorio_datos = directorio_datos
        self.resultados = {}
        
        # Crear directorio para gráficos
        os.makedirs('graficos', exist_ok=True)
        
    def cargar_datos(self, nombre_archivo):
        """
        Carga un archivo CSV con manejo de errores
        
        Args:
            nombre_archivo: Nombre del archivo CSV a cargar
            
        Returns:
            DataFrame con los datos o None si hay error
        """
        try:
            ruta_completa = os.path.join(self.directorio_datos, nombre_archivo)
            
            # Verificar si el archivo existe
            if not os.path.exists(ruta_completa):
                raise FileNotFoundError(f"Error: El archivo {ruta_completa} no existe")
            
            # Cargar datos
            df = pd.read_csv(ruta_completa)
            print(f"✅ Archivo {nombre_archivo} cargado correctamente")
            return df
            
        except FileNotFoundError as e:
            print(f"❌ {str(e)}")
            return None
        except pd.errors.EmptyDataError:
            print(f"❌ Error: El archivo {nombre_archivo} está vacío")
            return None
        except Exception as e:
            print(f"❌ Error inesperado al cargar {nombre_archivo}: {str(e)}")
            return None
    
    def analizar_categoria(self, df, categoria):
        """
        Analiza una categoría específica de productos
        
        Args:
            df: DataFrame con los datos de la tienda
            categoria: Nombre de la categoría a analizar
            
        Returns:
            Diccionario con resultados del análisis
        """
        try:
            # Filtrar por categoría
            df_cat = df[df['Categoría del Producto'] == categoria]
            
            if df_cat.empty:
                print(f"⚠️ No hay datos para la categoría {categoria}")
                return {}
            
            # Análisis de la categoría
            resultados = {
                'Total Ventas': df_cat['Precio'].sum(),
                'Cantidad Productos': len(df_cat),
                'Precio Promedio': df_cat['Precio'].mean(),
                'Producto Más Vendido': df_cat['Producto'].value_counts().idxmax(),
                'Calificación Promedio': df_cat['Calificación'].mean(),
                'Costo Envío Promedio': df_cat['Costo de envío'].mean()
            }
            
            # Top 3 productos más vendidos
            resultados['Top Productos'] = df_cat['Producto'].value_counts().head(3).index.tolist()
            
            # Coordenada más repetida
            coord_mas_repetida = df_cat.groupby(['lat', 'lon']).size().idxmax()
            resultados['Coordenada Más Repetida'] = f"({coord_mas_repetida[0]}, {coord_mas_repetida[1]})"
            
            return resultados
            
        except KeyError as e:
            print(f"❌ Error: Columna {e} no encontrada en los datos")
            return {}
        except Exception as e:
            print(f"❌ Error al analizar categoría {categoria}: {str(e)}")
            return {}
    
    def graficar_categoria(self, df, categoria, nombre_tienda):
        """Genera gráficos para una categoría específica"""
        try:
            # Filtrar por categoría
            df_cat = df[df['Categoría del Producto'] == categoria]
            
            if df_cat.empty:
                print(f"⚠️ No hay datos para graficar la categoría {categoria}")
                return
            
            # Crear figura con subplots
            fig, axes = plt.subplots(2, 2, figsize=(15, 10))
            fig.suptitle(f'Análisis de {categoria} en {nombre_tienda}', fontsize=16)
            
            # 1. Productos más vendidos
            productos = df_cat['Producto'].value_counts().head(5)
            productos.plot(kind='bar', ax=axes[0, 0], color='blue')
            axes[0, 0].set_title(f'Top 5 Productos - {categoria}')
            axes[0, 0].set_ylabel('Cantidad Vendida')
            axes[0, 0].tick_params(axis='x', rotation=45)
            
            # 2. Distribución de calificaciones
            df_cat['Calificación'].value_counts().sort_index().plot(kind='bar', ax=axes[0, 1], color='green')
            axes[0, 1].set_title('Distribución de Calificaciones')
            axes[0, 1].set_xlabel('Calificación')
            axes[0, 1].set_ylabel('Cantidad')
            
            # 3. Precios promedio por producto
            precio_por_producto = df_cat.groupby('Producto')['Precio'].mean().sort_values(ascending=False).head(5)
            precio_por_producto.plot(kind='barh', ax=axes[1, 0], color='red')
            axes[1, 0].set_title('Precio Promedio - Top 5 Productos')
            axes[1, 0].set_xlabel('Precio Promedio')
            
            # 4. Método de pago
            df_cat['Método de pago'].value_counts().plot(kind='pie', ax=axes[1, 1], autopct='%1.1f%%')
            axes[1, 1].set_title('Métodos de Pago')
            
            plt.tight_layout(rect=[0, 0, 1, 0.95])
            plt.savefig(f"graficos/{nombre_tienda}_{categoria.replace(' ', '_')}.png")
            plt.close()  # Cerrar figura para evitar consumo excesivo de memoria
            
            print(f"📊 Gráfico de {categoria} generado en {nombre_tienda}")
            
        except Exception as e:
            print(f"❌ Error al graficar categoría {categoria}: {str(e)}")
            plt.close()  # Asegurar que la figura se cierre incluso en caso de error
    
    def graficar_comparativa_categorias(self, resultados_tienda, nombre_tienda):
        """Genera un gráfico comparativo entre las categorías de una tienda"""
        try:
            # Preparar datos
            categorias = []
            ingresos = []
            
            for cat, datos in resultados_tienda.items():
                if 'Total Ventas' in datos:
                    categorias.append(cat)
                    ingresos.append(datos['Total Ventas'])
            
            if not categorias:
                return
                
            # Crear gráfico
            plt.figure(figsize=(12, 6))
            plt.bar(categorias, ingresos, color='skyblue')
            plt.title(f'Ingresos por Categoría - {nombre_tienda}')
            plt.ylabel('Ingresos Totales')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(f"graficos/{nombre_tienda}_categorias.png")
            plt.close()  # Cerrar figura para evitar consumo excesivo de memoria
            
        except Exception as e:
            print(f"❌ Error al generar comparativa de categorías: {str(e)}")
            plt.close()  # Asegurar que la figura se cierre incluso en caso de error
    
    def analizar_tienda(self, nombre_tienda):
        """Analiza una tienda completa, procesando cada categoría independientemente"""
        try:
            print(f"\n{'='*50}")
            print(f"🏪 ANALIZANDO {nombre_tienda.upper()}")
            print(f"{'='*50}")
            
            # Cargar datos
            df = self.cargar_datos(f"tienda_{nombre_tienda[-1]}.csv")
            if df is None:
                return {}
            
            # Obtener categorías únicas
            categorias = df['Categoría del Producto'].unique()
            print(f"📋 Categorías encontradas: {len(categorias)}")
            print(f"   {', '.join(categorias)}")
            
            # Análisis general
            resultados_tienda = {
                'ingresos_totales': df['Precio'].sum(),
                'calificacion_promedio': df['Calificación'].mean(),
                'productos_total': len(df),
                'categorias': {}
            }
            
            # Analizar cada categoría individualmente
            for categoria in categorias:
                print(f"\n📝 Analizando categoría: {categoria}")
                
                try:
                    # Análisis de la categoría
                    resultados_categoria = self.analizar_categoria(df, categoria)
                    
                    # Mostrar resultados
                    if resultados_categoria:
                        print(f"  • Producto más vendido: {resultados_categoria.get('Producto Más Vendido', 'N/A')}")
                        print(f"  • Total ventas: ${resultados_categoria.get('Total Ventas', 0):,.2f}")
                        print(f"  • Calificación promedio: {resultados_categoria.get('Calificación Promedio', 0):.2f}/5")
                    
                    # Guardar resultados
                    resultados_tienda['categorias'][categoria] = resultados_categoria
                    
                    # Generar gráficos
                    self.graficar_categoria(df, categoria, nombre_tienda)
                    
                except Exception as e:
                    print(f"❌ Error procesando categoría {categoria}: {str(e)}")
                    continue
            
            # Graficar comparativa entre categorías
            self.graficar_comparativa_categorias(resultados_tienda['categorias'], nombre_tienda)
            
            # Guardar resultados
            self.resultados[nombre_tienda] = resultados_tienda
            return resultados_tienda
            
        except Exception as e:
            print(f"❌ Error al analizar tienda {nombre_tienda}: {str(e)}")
            traceback.print_exc()
            return {}
    
    def generar_recomendacion(self):
        """Genera recomendación sobre qué tienda vender"""
        try:
            if len(self.resultados) < 2:
                print("⚠️ Se necesitan al menos dos tiendas para generar recomendación")
                return
                
            print("\n\n📋 GENERANDO RECOMENDACIÓN FINAL...")
            
            # Métricas para la decisión
            metricas = {}
            for tienda, datos in self.resultados.items():
                metricas[tienda] = {
                    'ingresos': datos.get('ingresos_totales', 0),
                    'calificacion': datos.get('calificacion_promedio', 0),
                    'puntuacion': 0  # Inicializar puntuación
                }
            
            # Calcular puntuación (mayor es mejor)
            for tienda, datos in metricas.items():
                # 60% por ingresos, 40% por calificación
                ingresos_rel = datos['ingresos'] / max(m['ingresos'] for m in metricas.values()) if max(m['ingresos'] for m in metricas.values()) > 0 else 0
                calif_rel = datos['calificacion'] / 5  # Normalizado a 5
                
                datos['puntuacion'] = (ingresos_rel * 0.6) + (calif_rel * 0.4)
            
            # Ordenar tiendas por puntuación (menor a mayor)
            tiendas_ordenadas = sorted(metricas.items(), key=lambda x: x[1]['puntuacion'])
            
            # La tienda con menor puntuación es candidata para vender
            tienda_vender = tiendas_ordenadas[0][0]
            
            # Mostrar recomendación
            print("\n" + "="*60)
            print(f" RECOMENDACION FINAL: Vender {tienda_vender}")
            print("="*60)
            
            # Guardar recomendación
            with open('recomendacion_final.txt', 'w') as f:
                f.write(f"RECOMENDACION: Vender {tienda_vender}\n\n")
                for tienda, datos in tiendas_ordenadas:
                    f.write(f"{tienda}:\n")
                    f.write(f"   Ingresos: ${datos['ingresos']:,.2f}\n")
                    f.write(f"   Calificacion: {datos['calificacion']:.2f}/5\n")
                    f.write(f"   Puntuacion: {datos['puntuacion']:.2f}\n\n")
            
            print(" Recomendacion guardada en 'recomendacion_final.txt'")
            
        except Exception as e:
            print(f" Error al generar recomendación: {str(e)}")
            traceback.print_exc()

    def exportar_excel(self, nombre_archivo="resumen_tiendas.xlsx"):
        """
        Exporta los resultados del análisis a un archivo Excel
        
        Args:
            nombre_archivo: Nombre del archivo Excel a generar
        """
        try:
            print(f"\n Exportando resultados a Excel: {nombre_archivo}")
            
            with pd.ExcelWriter(nombre_archivo) as writer:
                # Para cada tienda
                for tienda, datos in self.resultados.items():
                    # Crear dataframe resumen general
                    resumen_tienda = pd.DataFrame({
                        'Ingresos Totales': [datos['ingresos_totales']],
                        'Calificación Promedio': [datos['calificacion_promedio']],
                        'Productos Totales': [datos['productos_total']]
                    })
                    
                    # Guardar resumen general
                    resumen_tienda.to_excel(writer, sheet_name=f"{tienda}_Resumen", index=False)
                    
                    # Crear dataframe para cada categoría
                    categorias_data = []
                    for categoria, cat_datos in datos['categorias'].items():
                        if cat_datos:
                            row = {'Categoría': categoria}
                            row.update(cat_datos)
                            categorias_data.append(row)
                    
                    if categorias_data:
                        df_categorias = pd.DataFrame(categorias_data)
                        df_categorias.to_excel(writer, sheet_name=f"{tienda}_Categorias", index=False)
            
            print(f" Archivo Excel '{nombre_archivo}' generado correctamente")
            
        except Exception as e:
            print(f" Error al exportar a Excel: {str(e)}")
            traceback.print_exc()

def main():
    """Función principal"""
    try:
        # Crear instancia del analizador
        analizador = AnalisisTienda()
        
        # Analizar cada tienda
        for i in range(1, 5):
            analizador.analizar_tienda(f"Tienda {i}")
        
        # Generar recomendación
        analizador.generar_recomendacion()
        
        # Exportar a Excel
        analizador.exportar_excel()
        
        print("\n Análisis completado con éxito")
        
    except Exception as e:
        print(f" Error en ejecución principal: {str(e)}")
        traceback.print_exc()

if __name__ == "__main__":
    main()
