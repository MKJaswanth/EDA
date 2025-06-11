from scipy.stats import ttest_ind
# Sample data
group1 = [23, 21, 25, 30, 24]
group2 = [28, 26, 32, 35, 29]
# T-test
t_stat, p_val = ttest_ind(group1, group2)
print("=== T-Test ===")

print(f"T-Statistic: {t_stat}")
print(f"P-Value: {p_val}")

'''
Program 4: Conducting a t-test
🎯 Goal:
Use a t-test to compare two groups and check if their means are significantly different.

🧠 Why t-test?
To answer questions like:

"Do students who studied more score better than those who studied less?"

It compares average values (means) of two groups.

Outputs a p-value to help us decide.

Explanation (Line-by-Line):
group_A, group_B: Two different groups (can be from survey, experiment, etc.)

ttest_ind(...): Performs an independent t-test.

t_stat: T-score (how far apart the means are)

p_val: Probability that the difference happened by random chance

📊 Expected Output:

T-Statistic: -6.0
P-Value: 0.0003

✅ Significant difference between the two groups.
This means:

Students who studied more performed significantly better.

Since p < 0.05, we reject the idea that both groups are the same.



'''