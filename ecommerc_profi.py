from readline import redisplay
import pandas as pd

# Load the dataset
data = pd.read_csv('E-commerce Dataset.csv')

# Display basic info
print(data.info())

# Handle missing values
data = data.dropna()  # Drop rows with missing values (or use fillna for imputation)

# Remove duplicates
data = data.drop_duplicates()

# Convert columns to appropriate data types if necessary
data['Date'] = pd.to_datetime(data['Order_Date'])  # Example: Convert a date column

# Save the cleaned data for further analysis
data.to_csv('cleaned_dataset.csv', index=False)
print("Data cleaning completed. Cleaned dataset saved.")

# Display the first few rows of the cleaned dataset
print(data.head())

# Display summary statistics to understand the dataset
print(data.describe())

