import pandas as pd

def eliminar_nulos(df):
    """Elimina las filas con valores nulos de un DataFrame"""
    return df.dropna()

def normalizar(df, columnas):
    """Normaliza las columnas seleccionadas de un DataFrame"""
    df[columnas] = (df[columnas] - df[columnas].min()) / (df[columnas].max() - df[columnas].min())
    return df