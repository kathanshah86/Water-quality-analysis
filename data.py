import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate random values for 100 samples
n_samples = 100
data = {
    'pH': np.round(np.random.uniform(5.5, 8.5, n_samples), 2),  # pH range 5.5 to 8.5
    'Turbidity (NTU)': np.round(np.random.uniform(1, 10, n_samples), 2),  # Turbidity 1 to 10 NTU
    'DO (mg/L)': np.round(np.random.uniform(2, 10, n_samples), 2),  # DO 2 to 10 mg/L
    'Temperature (°C)': np.random.randint(15, 30, n_samples),  # Temperature 15 to 30°C
}

# Create a DataFrame
df = pd.DataFrame(data)

# Rule-based Quality Labeling
def classify_quality(row):
    if 6.5 <= row['pH'] <= 8.5 and row['Turbidity (NTU)'] <= 5 and row['DO (mg/L)'] >= 6:
        return 'Good'
    elif row['Turbidity (NTU)'] > 8 or row['DO (mg/L)'] < 4 or row['pH'] < 6.0:
        return 'Polluted'
    else:
        return 'Moderate'

# Apply classification
df['Quality'] = df.apply(classify_quality, axis=1)

# Save to CSV
df.to_csv('water_quality_data.csv', index=False)

print("Dataset with 100 rows has been generated and saved as 'water_quality_data_100.csv'.")
print(df.head())
