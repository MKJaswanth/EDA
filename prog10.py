import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
 'Experience': [1, 2, 1, 3, 2],
 'Salary': [50000, 60000, 55000, 70000, 65000],
 'Age': [22, 25, 24, 28, 26]
})
sns.pairplot(df)
plt.suptitle("Multivariate Analysis", y=1.02)
plt.show()

'''
Program 10: Multivariate Analysis
🎯 Goal:
Analyze three or more variables at once to understand complex relationships.

🧠 What is Multivariate Analysis?
“Multi” means more than two.

Helps answer:

How do multiple factors together affect a result?

Is one variable more influential than another?

Common tools:

Pair plots

Heatmaps (correlation matrix)

Multivariate regression

Explanation of the Code:
Part	What It Does
df.corr()	Calculates correlation between all pairs of numerical columns
sns.heatmap()	Visually shows how strongly each pair of variables are correlated
sns.pairplot()	Shows scatterplots, histograms, and relationships between all variables at once

📊 Sample Output (Printed Correlation Matrix):

📋 Correlation Matrix:
               Hours_Studied  Sleep_Hours  Exam_Score
Hours_Studied         1.000        -0.99        0.99
Sleep_Hours          -0.99         1.000       -0.99
Exam_Score            0.99        -0.99        1.000
Hours studied ⬆️ → Exam score ⬆️

Sleep hours ⬆️ → Exam score ⬇️ (possibly less study time)

👦 Think Like a Kid:
“I study more, I get higher marks, but if I sleep too much, I might not have time to study. Multivariate analysis helps me understand how all three things together affect my exam.”

'''