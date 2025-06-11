import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({'X': [10, 20, 30, 40, 50, 60, 55, 65, 45]})
sns.histplot(df['X'], kde=True, color='purple')
plt.title("Univariate Analysis")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

'''
Program 8: Univariate Analysis
🎯 Goal:
Understand and analyze one variable at a time — this is called univariate analysis.

🧠 What is Univariate Analysis?
“Uni” means one.

So, univariate analysis is the statistical analysis of a single variable.

Helps you explore:

Central tendency (mean, median, mode)

Spread (variance, standard deviation, range)

Distribution shape (skewness, kurtosis)

Visualization (histograms, boxplots)
 Explanation of Each Part:
Part	Explanation
describe()	Gives summary: count, mean, std, min, max, quartiles
mean(), median(), mode()	Measures of central tendency
std(), var()	Measures of spread
skew()	Tells if data is left or right skewed
kurt()	Tells how peaked or flat the distribution is
histplot()	Shows distribution (like bell-curve)
boxplot()	Shows median, IQR, and outliers visually

📊 Sample Output:

📋 Descriptive Statistics:
count    10.000000
mean     21.000000
std       1.825742
min      18.000000
25%      19.250000
50%      21.000000
75%      22.000000
max      24.000000

🧠 Mean: 21.0
🧠 Median: 21.0
🧠 Mode: 22

📈 Standard Deviation: 1.825742
📈 Variance: 3.333333

📊 Skewness: -0.194
📊 Kurtosis: -1.054
🧒 Think Like a Kid:
"Univariate analysis is like checking one student’s test marks — understanding how high, low, or average they are — and drawing a graph to show it."
'''