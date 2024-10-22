# carga_datos.py
import pandas as pd


def cargar_financieros(ruta):
    """Carga un archivo CSV de datos financieros"""
    return pd.read_csv(ruta, parse_dates=['fecha'])
