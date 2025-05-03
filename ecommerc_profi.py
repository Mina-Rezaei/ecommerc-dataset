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

# Function to remove outliers using the IQR method
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)  # First quartile
    Q3 = df[column].quantile(0.75)  # Third quartile
    IQR = Q3 - Q1  # Interquartile range
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Remove outliers from Profit, Sales, and Discount columns
data = remove_outliers(data, 'Profit')
data = remove_outliers(data, 'Sales')
data = remove_outliers(data, 'Discount')

# Data Type Handling
# Convert numerical columns to float or integer (coerce invalids to NaN)
numerical_columns = ['Sales', 'Profit', 'Discount', 'Quantity', 'Shipping_Cost']
for col in numerical_columns:
    if col in data.columns:
        data[col] = pd.to_numeric(data[col], errors='coerce')
    else:
        print(f"Warning: Numerical column '{col}' not found in DataFrame.")

# Create 'Date' column by combining Order_Date and Time
if 'Order_Date' in data.columns and 'Time' in data.columns:
    data['Date'] = pd.to_datetime(data['Order_Date'].astype(str) + ' ' + data['Time'].astype(str), errors='coerce')
else:
    print("Warning: 'Order_Date' or 'Time' column not found. Skipping Date conversion.")

# Convert Customer_Id to object (string)
if 'Customer_Id' in data.columns:
    data['Customer_Id'] = data['Customer_Id'].astype('object')
else:
    print("Warning: 'Customer_Id' column not found.")

# Convert categorical columns to 'category' dtype
categorical_columns = [
    'Gender',
    'Device_Type',
    'Customer_Login_type',
    'Product_Category',
    'Order_Priority',
    'Payment_method'
]

for col in categorical_columns:
    if col in data.columns:
        data[col] = data[col].astype('category')
    else:
        print(f"Warning: Categorical column '{col}' not found in DataFrame.")

# Feature Engineering: Extract Month and Quarter, and calculate Profit Margin
data['Month'] = data['Order_Date'].dt.month
data['Quarter'] = data['Order_Date'].dt.quarter
data['Profit_Margin'] = data['Profit'] / data['Sales']

# Save the cleaned data for further analysis
data.to_csv('cleaned_dataset.csv', index=False)
print("Data cleaning completed. Cleaned dataset saved.")

# Display the first few rows of the cleaned dataset
print(data.head())

# Display summary statistics to understand the dataset
print(data.describe())

# Display the number of rows in the dataset
print(f"Number of rows in the dataset: {len(data)}")
