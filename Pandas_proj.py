import pandas as pd

# Load the Titanic dataset from an online source
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# Show the first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Basic info about dataset (columns, data types, missing values)
print("\nDataset info:")
print(df.info())

# Summary statistics for numerical columns
print("\nSummary statistics:")
print(df.describe())

# Count of survivors vs non-survivors
print("\nSurvival counts:")
print(df['Survived'].value_counts())

# Calculate survival rate
survival_rate = df['Survived'].mean()
print(f"\nSurvival rate: {survival_rate:.2f}")

# Filter passengers who survived and were female
females_survived = df[(df['Survived'] == 1) & (df['Sex'] == 'female')]
print(f"\nNumber of females who survived: {len(females_survived)}")

# Average age of passengers
avg_age = df['Age'].mean()
print(f"\nAverage age of passengers: {avg_age:.2f}")

# Fill missing ages with the average age
df['Age'] = df['Age'].fillna(avg_age)

# Show updated info (no more missing ages)
print("\nUpdated dataset info after filling missing ages:")
print(df.info())
