import pandas as pd
from scipy.stats import pearsonr
# Creating a simple dataset
data = {'X': [10, 20, 30, 40, 50], 'Y': [15, 25, 35, 45, 60]}
df = pd.DataFrame(data)
# Calculating correlation and p-value
correlation, p_value = pearsonr(df['X'], df['Y'])
print("=== Correlation and P-Value ===")
print(f"Correlation coefficient: {correlation}")
print(f"P-value: {p_value}")

'''
✅ Program 1: Correlation and p-value Concepts
🎯 Goal:
Understand the relationship between two numeric variables using:

Correlation coefficient → Tells us how strongly two variables are related.

p-value → Tells us whether the relationship is statistically significant.

🧠 Concept Recap:
Correlation coefficient (r):

Ranges from -1 to 1

+1 → perfect positive relationship

-1 → perfect negative relationship

0 → no relationship

p-value:

If p < 0.05, the correlation is statistically significant (we trust it).

If p > 0.05, it might be due to chance.
 Explanation (Line-by-Line):
import pandas as pd: Import the pandas library for data handling.

from scipy.stats import pearsonr: Import the Pearson correlation function.

df = pd.DataFrame(data): Create a DataFrame with Hours_Studied and Test_Score.

pearsonr(...): Returns two values:

Correlation Coefficient

p-value

📈 Expected Output:

Correlation Coefficient: 0.991...
P-value: 0.000...

This means:

There is a very strong positive correlation between Hours_Studied and Test_Score.

The p-value is very small → the correlation is statistically significant.

'''