import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)
df = pd.DataFrame({
    'TV_Ad_Spend': np.random.uniform(50, 300, 150),
    'Radio_Ad_Spend': np.random.uniform(10, 50, 150),
    'Region': np.random.choice(['North', 'South', 'West', 'East'], 150)
})
df['Sales'] = 50 + df['TV_Ad_Spend'] * 0.9 + df['Radio_Ad_Spend'] * 1.3 + np.random.normal(0, 25, 150)
df.loc[df['Region'] == 'South', 'Sales'] += 30
# Build a full model with all our main predictors
full_model = smf.ols(formula='Sales ~ TV_Ad_Spend + Radio_Ad_Spend + C(Region)', data=df).fit()

# Print the full OLS summary for detailed interpretation
print("--- Full OLS Regression Results ---")
print(full_model.summary())
