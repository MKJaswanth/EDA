import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
df = pd.DataFrame({
    'TV_Ad_Spend':np.random.uniform(50, 300, 150),
    'Radio_Ad_Spend': np.random.uniform(10, 50, 150),
    'Region': np.random.choice(['North', 'South', 'West', 'East'], 150)
})
df['Sales'] = 50 + df['TV_Ad_Spend'] * 0.9 + df['Radio_Ad_Spend'] * 1.3 + np.random.normal(0, 25, 150)
df.loc[df['Region'] == 'South', 'Sales'] += 30
plt.scatter(df['TV_Ad_Spend'], df['Sales'])
plt.title('Sales vs. TV Ad Spend')
plt.xlabel('TV Ad Spend ($)')
plt.ylabel('Sales ($)')
plt.show()