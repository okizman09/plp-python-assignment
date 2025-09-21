"""
📊 Analyzing Data with Pandas and Visualizing Results with Matplotlib
By: Okiki
"""

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# -----------------------------
# Task 1: Load and Explore Data
# -----------------------------
iris = load_iris(as_frame=True)
df = iris.frame  # Convert to a DataFrame

print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nChecking missing values:")
print(df.isnull().sum())

# -----------------------------
# Task 2: Basic Data Analysis
# -----------------------------
print("\nStatistical Summary:")
print(df.describe())

grouped = df.groupby("target").mean()
print("\nMean values grouped by species:")
print(grouped)

# -----------------------------
# Task 3: Data Visualization
# -----------------------------

# 1. Line Chart (trend simulation)
df_sorted = df.sort_values("petal length (cm)")
df_sorted["petal length (cm)"].cumsum().plot(kind="line", figsize=(8,5))
plt.title("Cumulative Petal Length Trend")
plt.xlabel("Index")
plt.ylabel("Cumulative Petal Length (cm)")
plt.grid(True)
plt.show()

# 2. Bar Chart (average petal length by species)
sns.barplot(x="target", y="petal length (cm)", data=df, ci=None, palette="viridis")
plt.title("Average Petal Length by Species")
plt.xlabel("Species (0 = Setosa, 1 = Versicolor, 2 = Virginica)")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal length)
plt.hist(df["sepal length (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot (relationship between sepal length and petal length)
sns.scatterplot(
    x="sepal length (cm)", 
    y="petal length (cm)", 
    hue="target", 
    data=df, 
    palette="deep"
)
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# -----------------------------
# Findings and Observations
# -----------------------------
print("""
Findings:
1. The Iris dataset is clean and does not contain missing values.
2. Setosa has the smallest petal dimensions, while Virginica has the largest.
3. Bar chart shows petal length strongly differentiates species.
4. Histogram shows sepal length is normally distributed (~5.5 cm center).
5. Scatter plot shows Setosa is clearly separated, while Versicolor and Virginica overlap slightly.
""")
