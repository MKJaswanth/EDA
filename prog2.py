import matplotlib.pyplot as plt
import pandas as pd
# Sample data
data = {'X': [10, 20, 30, 40, 50], 'Y': [15, 25, 35, 45, 60]}
df = pd.DataFrame(data)
# Creating a scatterplot
plt.scatter(df['X'], df['Y'], color='green')
plt.title('Scatter Plot of X vs Y')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.grid(True)
plt.show()

'''
Program 2: Scatterplots
🎯 Goal:
Visualize the relationship between two numeric variables using a scatterplot.

🧠 Why Scatterplots?
Each dot shows a pair of values (x, y).

Helps us see:

Positive/Negative relationship

Linearity

Outliers

 Explanation (Line-by-Line):
import matplotlib.pyplot as plt: Used to plot graphs.

plt.scatter(...): Makes a scatterplot.

color='blue': Sets dot color.

xlabel, ylabel, title: Adds labels to make the graph understandable.

grid=True: Shows gridlines.

plt.show(): Displays the graph window.

📊 Expected Output:
A graph with:

X-axis: Hours Studied

Y-axis: Test Score

Dots arranged upward diagonally (showing positive relationship)

'''