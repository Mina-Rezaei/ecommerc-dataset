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
data['Date'] = pd.to_datetime(data['Order_Date'].astype(str) + ' ' + data['Time'].astype(str)) # Combine the Order_Date column and the Time column into a single new datetime column.
data['Quantity'] = data['Quantity'].astype('Int64')  # Convert Quantity to integer
data['Customer_Id'] = data['Customer_Id'].astype('object')  # Convert int64 to string
columns_to_convert = [
    'Gender',
    'Device_Type',
    'Customer_Login_type',
    'Product_Category',
    'Order_Priority',
    'Payment_method'
]

# Loop through the columns and change their type to 'category'
for col in columns_to_convert:
    if col in data.columns: 
        data[col] = data[col].astype('category')
    else:
        print(f"Warning: Column '{col}' not found in DataFrame.")

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

print(data.head())  # Display the first few rows of the cleaned data
