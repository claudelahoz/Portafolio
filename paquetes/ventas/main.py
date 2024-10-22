from load_data import DataLoader
from clean_data import DataCleaner
from visualize_data import DataVisualizer

def main():
    """
    Función principal que ejecuta el análisis de datos de ventas de licores
    """
    # Inicializar las clases
    loader = DataLoader()
    cleaner = DataCleaner()
    visualizer = DataVisualizer()
    
    # Cargar datos
    df = loader.load_csv('liquor_sales.csv')
    
    if df is not None:
        # Limpiar datos
        df_clean = cleaner.clean_data(df)
        
        # Guardar datos limpios
        loader.save_csv(df_clean, 'liquor_sales_clean.csv')
        
        # Crear visualizaciones
        visualizer.plot_sales_by_category(df_clean)
        visualizer.plot_sales_trend(df_clean)
        visualizer.plot_top_vendors(df_clean)
        
        # Imprimir resumen estadístico
        print("\nResumen estadístico de ventas:")
        print(df_clean['Sale (Dollars)'].describe())
        
        print("\nAnálisis completado exitosamente!")
    else:
        print("No se pudo completar el análisis debido a errores en la carga de datos.")

if __name__ == "__main__":
    main()