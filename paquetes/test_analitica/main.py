import pandas as pd
#from analisis_datos import eliminar_nulos, normalizar, grafico_barras, grafico_correlacion
from analisis_datos.limpieza import eliminar_nulos, normalizar
from analisis_datos.visualizacion import grafico_barras, grafico_correlacion

# Carga de datos
ruta = "C:/Users/delahozce/OneDrive - GLOBAL HITSS/Documentos/Proyectos/Codes/git_portafolio/Portafolio/paquetes"
df = pd.read_csv(ruta + "/test_analitica/data.csv")


# Limpieza de datos y normalización
df_limpio = eliminar_nulos(df)
df_normalizado = normalizar(df_limpio, ['age', 'salary'])

# Visualización de datos
grafico_barras(df_normalizado, 'gender')
grafico_correlacion(df_normalizado,)

