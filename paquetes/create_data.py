import pandas as pd
import numpy as np

# Generating a synthetic dataset for financial data
np.random.seed(42)

# Date range
dates = pd.date_range(start='2022-01-01', periods=100)

# Simulated financial data
precio_cierre = np.random.normal(loc=150, scale=10, size=len(dates))  # Closing prices
volumen = np.random.randint(low=1000, high=5000, size=len(dates))     # Volume of transactions

# Creating a DataFrame
data = {
    'fecha': dates,
    'precio_cierre': precio_cierre,
    'volumen': volumen
}

df_financiero = pd.DataFrame(data)

# Saving to CSV
df_financiero.to_csv('datos_financieros_2.csv', index=False)

print(df_financiero.head())
