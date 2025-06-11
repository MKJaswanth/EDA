import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.DataFrame({
 'Salary': [50000, 60000, 55000, 70000, 65000],
 'Experience': [1, 2, 1, 3, 2],
 'Gender': ['Male', 'Female', 'Female', 'Male', 'Male']
})
# Dummy encode
df_encoded = pd.get_dummies(df, drop_first=True)

X = df_encoded[['Experience', 'Gender_Male']]
y = df_encoded['Salary']
model = LinearRegression()
model.fit(X, y)
print("=== MLR with Dummy Codes ===")
print(f"Intercept: {model.intercept_}")
print(f"Coefficients: {model.coef_}")
