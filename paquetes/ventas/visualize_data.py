import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    """
    Clase para visualización de datos de ventas de licores
    """
    def __init__(self):
        """
        Inicializa el visualizador de datos
        """
        self.set_style()
    
    def set_style(self):
        """
        Configura el estilo de las visualizaciones
        """
        plt.style.use('seaborn')
        sns.set_palette("husl")
        plt.rcParams['figure.figsize'] = (12, 6)
    
    def plot_sales_by_category(self, df, save_path=None):
        """
        Crea un gráfico de barras de ventas por categoría
        
        Args:
            df (pd.DataFrame): DataFrame con los datos
            save_path (str, optional): Ruta para guardar el gráfico
        """
        plt.figure(figsize=(12, 6))
        ventas_categoria = df.groupby('Category Name')['Sale (Dollars)'].sum().sort_values(ascending=False)
        
        ax = ventas_categoria.plot(kind='bar')
        plt.title('Ventas totales por categoría de licor')
        plt.xlabel('Categoría')
        plt.ylabel('Ventas totales ($)')
        plt.xticks(rotation=45, ha='right')
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
        plt.show()
    
    def plot_sales_trend(self, df, save_path=None):
        """
        Crea un gráfico de línea de tendencia de ventas mensuales
        
        Args:
            df (pd.DataFrame): DataFrame con los datos
            save_path (str, optional): Ruta para guardar el gráfico
        """
        plt.figure(figsize=(12, 6))
        ventas_mensuales = df.groupby([df['Date'].dt.to_period('M')])['Sale (Dollars)'].sum()
        
        ax = ventas_mensuales.plot(kind='line', marker='o')
        plt.title('Tendencia de ventas mensuales')
        plt.xlabel('Mes')
        plt.ylabel('Ventas ($)')
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
        plt.show()
    
    def plot_top_vendors(self, df, top_n=10, save_path=None):
        """
        Crea un gráfico de los principales vendedores
        
        Args:
            df (pd.DataFrame): DataFrame con los datos
            top_n (int): Número de vendedores a mostrar
            save_path (str, optional): Ruta para guardar el gráfico
        """
        plt.figure(figsize=(12, 6))
        top_vendors = df.groupby('Vendor Name')['Sale (Dollars)'].sum().nlargest(top_n)
        
        ax = top_vendors.plot(kind='barh')
        plt.title(f'Top {top_n} Vendedores por Ventas')
        plt.xlabel('Ventas totales ($)')
        plt.ylabel('Vendedor')
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
        plt.show()