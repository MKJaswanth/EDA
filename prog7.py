import pandas as pd
import statsmodels.api as sm

# Sample dataset
data = {
    'Hours_Studied': [2, 4, 6, 8, 10],
    'Test_Score': [50, 55, 65, 70, 80]
}

# Create DataFrame
df = pd.DataFrame(data)

# Define X and y
X = df['Hours_Studied']
y = df['Test_Score']

# Convert X to 2D and add constant
X = sm.add_constant(X)  # Adds the intercept term

# Fit the model
model = sm.OLS(y, X).fit()

# Show the summary
print(model.summary())
