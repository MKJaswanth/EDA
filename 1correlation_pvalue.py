import pandas as pd
import numpy as np
import scipy.stats as stats
np.random.seed(42)
df = pd.DataFrame({
    'TV_Ad_Spend': np.random.uniform(50, 300, 150),
    'Radio_Ad_Spend': np.random.uniform(10, 50, 150),
    'Region': np.random.choice(['North', 'South', 'West', 'East'], 150)
})
df['Sales'] = 50 + df['TV_Ad_Spend'] * 0.9 + df['Radio_Ad_Spend'] * 1.3 + np.random.normal(0, 25, 150)
df.loc[df['Region'] == 'South', 'Sales'] += 30
tv_spend = df['TV_Ad_Spend']
sales = df['Sales']
correlation_coefficient, p_value = stats.pearsonr(tv_spend, sales)
print(f"Correlation Coefficient: {correlation_coefficient:.4f}\nP-value: {p_value:.4f}")