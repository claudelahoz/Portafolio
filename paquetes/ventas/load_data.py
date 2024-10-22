import pandas as pd
from pathlib import Path

class DataLoader:
    """
    Clase para cargar y guardar datos de ventas de licores
    """
    def __init__(self, data_dir="data"):
        """
        Inicializa el cargador de datos
        
        Args:
            data_dir (str): Directorio donde se encuentran los datos
        """
        self.data_dir = Path(data_dir)
        
    def load_csv(self, filename, **kwargs):
        """
        Carga datos desde un archivo CSV
        
        Args:
            filename (str): Nombre del archivo CSV
            **kwargs: Argumentos adicionales para pd.read_csv
            
        Returns:
            pd.DataFrame: DataFrame con los datos cargados
        """
        file_path = self.data_dir / filename
        try:
            df = pd.read_csv(file_path, **kwargs)
            print(f"Datos cargados exitosamente de {file_path}")
            print(f"Dimensiones del dataset: {df.shape}")
            return df
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
            return None
    
    def save_csv(self, df, filename, **kwargs):
        """
        Guarda datos en un archivo CSV
        
        Args:
            df (pd.DataFrame): DataFrame a guardar
            filename (str): Nombre del archivo de salida
            **kwargs: Argumentos adicionales para df.to_csv
        """
        file_path = self.data_dir / filename
        try:
            df.to_csv(file_path, index=False, **kwargs)
            print(f"Datos guardados exitosamente en {file_path}")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")