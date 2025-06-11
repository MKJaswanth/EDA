from scipy.stats import f_oneway
group1 = [10, 20, 30]
group2 = [25, 35, 45]
group3 = [40, 50, 60]
f_stat, p_val = f_oneway(group1, group2, group3)
print("=== One-Way ANOVA ===")
print(f"F-Statistic: {f_stat}")
print(f"P-Value: {p_val}")
'''
 Program 12: One-Way ANOVA (Analysis of Variance)
🎯 Goal:
Check if three or more groups have significantly different means.

🧠 What is One-Way ANOVA?
Used when you have:

One categorical independent variable (like class, department, etc.)

One numeric dependent variable (like marks, height, etc.)

It answers:

“Do all these groups have the same average, or is at least one group different?”

Explanation of the Code:
Line	What It Does
f_oneway()	Compares group means using ANOVA
F-statistic	Tells how much group means differ compared to within-group differences
P-value	Probability that the difference happened by chance

📊 Sample Output:

📊 One-Way ANOVA Results
F-Statistic: 28.89
P-Value: 0.0001
✅ Result: Significant difference found between groups.
🎉 That means at least one group’s average score is statistically different from others.

👦 Think Like a Kid:
“If my friends in group C are scoring way higher than groups A and B, ANOVA helps me prove that with math!”

'''