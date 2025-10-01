import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

# ---- Data ----
np.random.seed(42)
df = pd.DataFrame({
    'TV_Ad_Spend': np.random.uniform(50, 300, 150),
    'Radio_Ad_Spend': np.random.uniform(10, 50, 150),
    'Region': np.random.choice(['North', 'South', 'West', 'East'], 150)
})
df['Sales'] = (
    50 + df['TV_Ad_Spend'] * 0.9 + df['Radio_Ad_Spend'] * 1.3
    + np.random.normal(0, 25, 150)
)
df.loc[df['Region'] == 'South', 'Sales'] += 30

# ---- Multiple Linear Regression ----
mlr = smf.ols('Sales ~ TV_Ad_Spend + C(Region)', data=df).fit()

# ---- Compact Output ----
print("\n--- Multiple Linear Regression Summary ---")
print("R-squared:", round(mlr.rsquared, 3))
print("Coefficients:\n", mlr.params.round(3))
print("\nP-values:\n", mlr.pvalues.round(4))
