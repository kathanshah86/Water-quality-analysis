# Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load Dataset
data = pd.read_csv('water_quality_data.csv')  # Ensure CSV file is present in the same folder
print("First 5 rows of the dataset:")
print(data.head())

# 2. Data Preprocessing
# Check for missing values
print("\nMissing Values in Each Column:")
print(data.isnull().sum())

# Descriptive Statistics
print("\nDescriptive Statistics:")
print(data.describe())

# 3. Ploting
# Histograms of Each Feature
data.hist(figsize=(10, 8), bins=20)
plt.suptitle('Feature Distributions')
plt.show()

# Boxplots for Outlier Analysis
plt.figure(figsize=(12, 6))
data.boxplot()
plt.title('Boxplot of All Features')
plt.show()

# Scatterplots: Relationships between Features
plt.figure(figsize=(8, 6))
plt.scatter(data['pH'], data['DO (mg/L)'], c='b', alpha=0.5)
plt.xlabel('pH')
plt.ylabel('Dissolved Oxygen (DO) in mg/L')
plt.title('pH vs Dissolved Oxygen')
plt.show()

# 4. Rule-based Water Quality Classification
# Define thresholds for classification
def classify_water_quality(row):
    if row['pH'] >= 6.5 and row['pH'] <= 8.5 and row['Turbidity (NTU)'] <= 5 and row['DO (mg/L)'] >= 6:
        return 'Good'
    elif row['Turbidity (NTU)'] > 8 or row['DO (mg/L)'] < 4:
        return 'Polluted'
    else:
        return 'Moderate'

# Apply the classification
data['Quality'] = data.apply(classify_water_quality, axis=1)

# Display classification results
print("\nUpdated Dataset with Quality Classification:")
print(data.head())

# 5. Visualization of Water Quality Distribution
plt.figure(figsize=(6, 4))
data['Quality'].value_counts().plot(kind='bar', color=['green', 'orange', 'red'])
plt.title('Water Quality Distribution')
plt.xlabel('Quality')
plt.ylabel('Count')
plt.show()

# 6. Insights and Summary
print("\nSummary of Water Quality Classification:")
print(data['Quality'].value_counts())
