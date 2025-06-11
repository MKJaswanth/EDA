import pandas as pd
df = pd.DataFrame({'X': [10, 20, 30, 40, 50, 60]})
print(df['X'].describe())

'''
 Program 11: Univariate Analysis (Categorical Data)
This is another example of univariate analysis, but this time, focusing on categorical (non-numeric) variables.

🧠 What is Categorical Univariate Analysis?
You're looking at only one variable, but it's not a number.

Examples:

Gender (Male, Female)

Grades (A, B, C)

Favorite subject (Math, English, Science)

We analyze frequency (how often something appears).

 Explanation of the Code:
Line	What It Does
value_counts()	Tells how many times each category appears
countplot()	Visualizes the count of each category

📊 Sample Output:

📊 Frequency of Favorite Subjects:
Math       3
Science    2
English    1
Name: Favorite_Subject, dtype: int64
✅ This tells us:

3 students love Math.

2 prefer Science.

1 likes English.

👧 Think Like a Kid:
“Let me check how many of my friends like Math or Science. Oh! Math is the most popular—cool!”
'''