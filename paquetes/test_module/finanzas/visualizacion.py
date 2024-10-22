# visualizacion.py
import matplotlib.pyplot as plt

def grafico_precios(df):
    """Genera un gráfico de los precios históricos"""
    plt.figure(figsize=(10, 6))
    plt.plot(df['fecha'], df['precio_cierre'], label='Precio de Cierre')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.title('Historial de Precios')
    plt.legend()
    plt.show()

def grafico_rendimiento(df):
    """Genera un gráfico del rendimiento porcentual diario"""
    plt.figure(figsize=(10, 6))
    plt.plot(df['fecha'], df['rendimiento_diario'], label='Rendimiento Diario')
    plt.xlabel('Fecha')
    plt.ylabel('Rendimiento Diario (%)')
    plt.title('Rendimiento Diario')
    plt.legend()
    plt.show()

def grafico_sma(df, ventana=10):
    """Genera un gráfico de la media móvil simple junto con los precios de cierre."""
    plt.figure(figsize=(10, 6))
    plt.plot(df['fecha'], df['precio_cierre'], label='Precio de Cierre')
    plt.plot(df['fecha'], df[f'SMA_{ventana}'], label=f'SMA {ventana} días')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.title(f'Precio de Cierre y SMA de {ventana} días')
    plt.legend()
    plt.show()

def grafico_rsi(df):
    """Genera un gráfico del Índice de Fuerza Relativa (RSI)."""
    plt.figure(figsize=(10, 6))
    plt.plot(df['fecha'], df['RSI'], label='RSI', color='purple')
    plt.axhline(70, linestyle='--', alpha=0.5, color='red', label='Sobrecomprado (70)')
    plt.axhline(30, linestyle='--', alpha=0.5, color='green', label='Sobrevendido (30)')
    plt.xlabel('Fecha')
    plt.ylabel('RSI')
    plt.title('Índice de Fuerza Relativa (RSI)')
    plt.legend()
    plt.show()

