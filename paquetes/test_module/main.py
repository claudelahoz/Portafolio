import finanzas

# 1. Cargar datos financieros desde un archivo CSV
df = finanzas.carga.cargar_financieros("D:/Consultoria/TalentoTech/NIVEL_AVANZADO/Modulos/Módulo3/paquetes/test_module/data_financiera.csv")


# 2. Calcular el rendimiento y la volatilidad
rendimiento = finanzas.calculos.calcular_rendimiento(df)
volatilidad = finanzas.calculos.calcular_volatilidad(df)

# Cálculos adicionales
df = finanzas.calculos.calcular_sma(df, ventana=20)  # SMA de 20 días
df = finanzas.calculos.calcular_rsi(df, periodo=14)  # RSI de 14 días
desviacion_volumen = finanzas.calculos.calcular_desviacion_volumen(df)

print(f"Rendimiento Anual: {rendimiento:.2%}")
print(f"Volatilidad Anual: {volatilidad:.2%}")
print(f"Desviación Estándar del Volumen: {desviacion_volumen:.2f}")

# 3. Visualización de precios y rendimiento
finanzas.visualizacion.grafico_precios(df)
finanzas.visualizacion.grafico_rendimiento(df)
finanzas.visualizacion.grafico_sma(df, ventana=20)
finanzas.visualizacion.grafico_rsi(df)
