import pandas as pd
from sklearn.linear_model import LinearRegression
# Creating a dataset
df = pd.DataFrame({'X': [10, 20, 30, 40, 50], 'Y': [15, 25, 35, 45, 60]})
X = df[['X']] # Features need to be 2D
y = df['Y']
# Creating the model and fitting
model = LinearRegression()
model.fit(X, y)
print("=== Linear Regression ===")
print(f"Intercept: {model.intercept_}")
print(f"Slope: {model.coef_[0]}")

'''
Program 3: Linear Regression
🎯 Goal:
Fit a straight line to the data that best describes the relationship between two variables using the y = mx + b formula.

🧠 Why Linear Regression?
It tells us:

How much y changes for each unit change in x

How well the line fits the data (R²)

Used to predict outcomes based on input variables.

📌 Formula Behind the Scenes:
y = mx + b

m = slope (how much y changes with x)

b = intercept (value of y when x = 0)
Explanation (Line-by-Line):
LinearRegression() creates the regression model.

.fit(X, y) learns the best-fit line.

.predict(X) calculates predicted scores.

model.coef_ gives slope, model.intercept_ gives intercept.

plt.plot(...) draws the regression line over the scatterplot.

📊 Expected Output:
You’ll see:

Blue dots = actual values

Red line = regression line

Console output shows:

Slope (m): ~4.79
Intercept (b): ~45.14
This means:

For each additional hour studied, the test score increases by about 4.79 points.

When hours studied is 0, the score starts at around 45.14.



'''