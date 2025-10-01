import pandas as pd
import numpy as np

def load_sales_data(seed=42):
    np.random.seed(seed)
    data = {
        'TV_Ad_Spend': np.random.uniform(50, 300, 150),
        'Radio_Ad_Spend': np.random.uniform(10, 50, 150),
        'Region': np.random.choice(['North', 'South', 'West', 'East'], 150)
    }
    df = pd.DataFrame(data)
    df['Sales'] = (50 + (df['TV_Ad_Spend'] * 0.9) + (df['Radio_Ad_Spend'] * 1.3) + np.random.normal(0, 25, 150))
    df.loc[df['Region'] == 'South', 'Sales'] += 30
    df['Sales'] = df['Sales'].round(2)
    return df
