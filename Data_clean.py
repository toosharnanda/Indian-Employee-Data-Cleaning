import pandas as pd
import numpy as np

# Load the employee dataset
df = pd.read_csv("part = 2/HANDLING MISSING VALUES/INDIAN EMPLOYEE DATASET/sample_data.csv", encoding="latin1")
print("Here's a quick look at the data:\n", df.head())

# Check missing values
print("\nMissing values per column:\n", df.isnull().sum())

# Fill missing salaries and performance ratings
df['SALARY(INR)'] = pd.to_numeric(df['SALARY(INR)'], errors='coerce')
df['PERFORMANCE RATING'] = pd.to_numeric(df['PERFORMANCE RATING'], errors='coerce')

df['SALARY(INR)'] = df['SALARY(INR)'].fillna(df['SALARY(INR)'].mean())
df['PERFORMANCE RATING'] = df['PERFORMANCE RATING'].fillna(df['PERFORMANCE RATING'].median())

print("\nAfter filling missing values, here are the first few rows:\n", df.head())

# Replace infinite values with NaN and remove duplicates
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.drop_duplicates(inplace=True)

# Fix negative salaries
neg_salaries = df[df['SALARY(INR)'] < 0]
if len(neg_salaries) > 0:
    print(f"\nFound {len(neg_salaries)} negative salaries. Replacing with mean salary.")
salary_mean = df['SALARY(INR)'].mean()
df['SALARY(INR)'] = np.where(df['SALARY(INR)'] < 0, salary_mean, df['SALARY(INR)'])

# Remove outliers using mean ± 3*std
std = df['SALARY(INR)'].std()
lower, upper = salary_mean - 3*std, salary_mean + 3*std
df = df[(df['SALARY(INR)'] >= lower) & (df['SALARY(INR)'] <= upper)]
print(f"\nRows after removing outliers: {len(df)}")

# Save the cleaned dataset
df.to_csv("CLEANED_INDIAN_EMPLOYEE_DATA.csv", index=False)
print("\nData cleaning done! Saved as 'CLEANED_INDIAN_EMPLOYEE_DATA.csv'")
