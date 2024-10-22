# calculos.py
import pandas as pd

def calcular_rendimiento(df):
    """Calcula el rendimiento porcentual diario y anualizado"""
    df['rendimiento_diario'] = df['precio_cierre'].pct_change()
    rendimiento_anual = df['rendimiento_diario'].mean() * 252
    return rendimiento_anual

def calcular_volatilidad(df):
    """Calcula la volatilidad anualizada"""
    df['rendimiento_diario'] = df['precio_cierre'].pct_change()
    volatilidad_diaria = df['rendimiento_diario'].std()
    volatilidad_anual = volatilidad_diaria * (252 ** 0.5)
    return volatilidad_anual

def calcular_sma(df, ventana=10):
    """Calcula la media móvil simple (SMA) sobre los precios de cierre."""
    df[f'SMA_{ventana}'] = df['precio_cierre'].rolling(window=ventana).mean()
    return df

def calcular_rsi(df, periodo=14):
    """Calcula el Índice de Fuerza Relativa (RSI) para los precios de cierre."""
    delta = df['precio_cierre'].diff()
    ganancia = delta.where(delta > 0, 0)
    perdida = -delta.where(delta < 0, 0)
    
    ganancia_media = ganancia.rolling(window=periodo).mean()
    perdida_media = perdida.rolling(window=periodo).mean()
    
    rs = ganancia_media / perdida_media
    rsi = 100 - (100 / (1 + rs))
    
    df['RSI'] = rsi
    return df

def calcular_desviacion_volumen(df):
    """Calcula la desviación estándar del volumen de operaciones."""
    desviacion_volumen = df['volumen'].std()
    return desviacion_volumen
