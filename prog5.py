import pandas as pd
# Categorical data
df_cat = pd.DataFrame({
 'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
 'Purchased': ['Yes', 'No', 'Yes', 'No', 'Yes']
})
# Count values
print(df_cat['Gender'].value_counts())
# Crosstab
print(pd.crosstab(df_cat['Gender'], df_cat['Purchased']))

'''
Program 5: Elucidate Categorical Features
🎯 Goal:
Understand and analyze categorical features (like Gender, Department, City) in a dataset.

🧠 Why Categorical Features Matter?
They represent categories or groups.

You can't do math directly on them.

Need to summarize or convert them (like with dummy coding in regression).


Explanation (Line-by-Line):
value_counts() shows how often each category appears.

unique() lists all different values.

pd.get_dummies() converts text categories into numbers so models can use them (aka One-Hot Encoding).

📊 Expected Output:

📋 Dataset:
      Name  Gender Department
0    Alice  Female         IT
1      Bob    Male         HR
2  Charlie    Male         IT
3    David    Male     Finance
4      Eve  Female         HR

🔢 Value counts for 'Gender':
Male      3
Female    2

🔢 Value counts for 'Department':
IT         2
HR         2
Finance    1

🔍 Unique values in 'Department':
['IT' 'HR' 'Finance']

📦 Dummy Variables (One-hot encoding):
   Dept_Finance  Dept_HR  Dept_IT
0             0        0        1
1             0        1        0
2             0        0        1
3             1        0        0
4             0        1        0
🤖 Why This Is Important for Machine Learning:
Algorithms can’t process words like "HR" or "Male".

We must convert them into numerical features using dummy variables or encoding.'''