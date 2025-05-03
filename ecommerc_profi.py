# 1. Data Cleaning and Preparation
from readline import redisplay
import pandas as pd
import matplotlib.pyplot as plt

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

# 2. Analysis Techniques
# Profit by Product Category

# Group by Product_Category and calculate total profit
category_profit = data.groupby('Product_Category')['Profit'].sum().sort_values(ascending=False)

# Bar chart for profit by category
category_profit.plot(kind='bar', figsize=(10, 6), title='Profit by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Profit')
plt.show()

