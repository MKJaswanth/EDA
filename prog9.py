import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({
 'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
 'Score': [70, 80, 75, 85, 90]
})
sns.boxplot(x='Gender', y='Score', data=df)
plt.title("Bivariate Analysis")
plt.show()

'''
 Program 9: Bivariate Statistics
🎯 Goal:
Analyze two variables together to understand their relationship.

🧠 What is Bivariate Analysis?
“Bi” = two variables.

It answers questions like:

Do these two variables move together?

If one goes up, does the other go up or down?

Techniques:

Covariance

Correlation

Scatterplots

Group-wise analysis (using groupby())
Explanation of Key Concepts:
Concept	What it Tells
Correlation	Strength & direction of linear relationship (value from -1 to +1)
Covariance	How two variables vary together (but not standardized)
Scatterplot	Visual way to spot patterns or trends
Group-wise stats	Helps compare categories (like low/high students)

📊 Sample Output:

📈 Correlation between Hours Studied and Exam Score: 0.99
📊 Covariance between Hours Studied and Exam Score: 18.60

📋 Average Exam Score by Student Type:
Student_Type
Average    61.5
High       69.0
Low        53.5
Name: Exam_Score, dtype: float64
👧 Think Like a Kid:
“If I study more hours, will I score more? Bivariate analysis helps me find that out by checking both together!”

'''
