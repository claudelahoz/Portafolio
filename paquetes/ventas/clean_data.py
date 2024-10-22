import pandas as pd
import numpy as np
from datetime import datetime

class DataCleaner:
    """
    Clase para limpiar y preprocesar datos de ventas de licores
    """
    def __init__(self):
        """
        Inicializa el limpiador de datos
        """
        self.numeric_columns = [
            'Bottle Volume (ml)', 'State Bottle Cost', 'State Bottle Retail',
            'Bottles Sold', 'Sale (Dollars)', 'Volume Sold (Liters)',
            'Volume Sold (Gallons)'
        ]
        self.categorical_columns = [
            'Store Name', 'County', 'Category Name', 'Vendor Name',
            'Item Description'
        ]
        
    def clean_data(self, df):
        """
        Realiza la limpieza completa de los datos
        
        Args:
            df (pd.DataFrame): DataFrame a limpiar
            
        Returns:
            pd.DataFrame: DataFrame limpio
        """
        # Hacer una copia para no modificar los datos originales
        df_clean = df.copy()
        
        # Convertir fecha
        df_clean['Date'] = pd.to_datetime(df_clean['Date'])
        
        # Limpiar valores numéricos
        for col in self.numeric_columns:
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
        
        # Eliminar duplicados
        df_clean = df_clean.drop_duplicates()
        
        # Rellenar valores nulos
        df_clean = self.fill_missing_values(df_clean)
        
        # Añadir columnas calculadas
        df_clean = self.add_calculated_columns(df_clean)
        
        return df_clean
    
    def fill_missing_values(self, df):
        """
        Rellena los valores faltantes en el DataFrame
        
        Args:
            df (pd.DataFrame): DataFrame con valores faltantes
            
        Returns:
            pd.DataFrame: DataFrame sin valores faltantes
        """
        # Rellenar valores numéricos con la media
        for col in self.numeric_columns:
            df[col] = df[col].fillna(df[col].mean())
        
        # Rellenar valores categóricos con 'Desconocido'
        for col in self.categorical_columns:
            df[col] = df[col].fillna('Desconocido')
        
        return df
    
    def add_calculated_columns(self, df):
        """
        Añade columnas calculadas útiles para el análisis
        
        Args:
            df (pd.DataFrame): DataFrame original
            
        Returns:
            pd.DataFrame: DataFrame con nuevas columnas
        """
        # Añadir columnas de tiempo
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month
        df['Day of Week'] = df['Date'].dt.day_name()
        
        # Calcular margen de beneficio
        df['Profit Margin'] = ((df['State Bottle Retail'] - df['State Bottle Cost']) / 
                             df['State Bottle Cost'] * 100)
        
        # Calcular precio por litro
        df['Price per Liter'] = df['Sale (Dollars)'] / df['Volume Sold (Liters)']
        
        return df