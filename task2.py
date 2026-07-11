import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. DATASET LOAD KARO - Task 1 wali cleaned file
df = pd.read_csv('cleaned_country_data.csv')

print("===== TASK 2: EXPLORATORY DATA ANALYSIS =====")
print("\n1. DATASET KA SHAPE:")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n2. DESCRIPTIVE STATISTICS:")
print(df.describe())

print("\n3. DATASET INFO:")
print(df.info())

print("\n4. NULL VALUES CHECK:")
print(df.isnull().sum())

# 5. TRENDS & DISTRIBUTIONS - GRAPHS
plt.figure(figsize=(15, 10))

# Graph 1: Population Distribution
plt.subplot(2, 3, 1)
sns.histplot(df['Population'], bins=30, kde=True)
plt.title('Population Distribution')
plt.xlabel('Population')

# Graph 2: GDP Distribution 
plt.subplot(2, 3, 2)
sns.histplot(df['GDP'], bins=30, kde=True)
plt.title('GDP Distribution')
plt.xlabel('GDP per capita')

# Graph 3: Literacy vs GDP - Relationship
plt.subplot(2, 3, 3)
sns.scatterplot(x='Literacy', y='GDP', data=df)
plt.title('Literacy vs GDP')
plt.xlabel('Literacy %')
plt.ylabel('GDP per capita')

# Graph 4: Top 10 Countries by Population
plt.subplot(2, 3, 4)
top_10_pop = df.nlargest(10, 'Population')
sns.barplot(x='Population', y='Country', data=top_10_pop)
plt.title('Top 10 Countries by Population')

# Graph 5: Boxplot for Outliers - GDP
plt.subplot(2, 3, 5)
sns.boxplot(x=df['GDP'])
plt.title('GDP Outliers Detection')
plt.xlabel('GDP per capita')

# Graph 6: Correlation Heatmap
plt.subplot(2, 3, 6)
numeric_df = df.select_dtypes(include=['float64', 'int64'])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')

plt.tight_layout()
plt.savefig('EDA_Graphs.png') # Graph save ho jayega
plt.show()

print("\n===== TASK 2 COMPLETE =====")
print("Graphs saved as 'EDA_Graphs.png'")
print("\nKEY FINDINGS:")
print(f"1. Highest GDP Country: {df.loc[df['GDP'].idxmax(), 'Country']}")
print(f"2. Highest Population Country: {df.loc[df['Population'].idxmax(), 'Country']}")
print(f"3. Average Literacy Rate: {df['Literacy'].mean():.2f}%")