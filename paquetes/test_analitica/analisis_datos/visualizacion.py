import matplotlib.pyplot as plt
import seaborn as sns

def grafico_barras(df, columna):
    """Genera un gráfico de barras para una columna categórica de un DataFrame"""
    plt.figure(figsize=(10, 6))
    sns.countplot(x=columna, data=df)
    plt.title(f'Distribución de la columna {columna}')
    plt.show()

def grafico_correlacion(df):
    """Genera un mapa de calor con la correlación entre las columnas numéricas de un DataFrame"""
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.select_dtypes(include=['float64', 'int64']).corr(), annot=True, cmap='coolwarm') #, annot=True, cmap='coolwarm'
    plt.title('Matriz de Correlación entre las columnas numéricas')
    plt.show()