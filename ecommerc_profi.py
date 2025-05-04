# 1. Data Cleaning and Preparation
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar



# Function to remove outliers using the IQR method
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)  # First quartile
    Q3 = df[column].quantile(0.75)  # Third quartile
    IQR = Q3 - Q1  # Interquartile range
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]



def main():
    # Placeholder for main function logic
    # Load the dataset
    df = pd.read_csv('E-commerce Dataset.csv')

    # Display basic info
    print(df.info())

    # Display column names
    print(df.columns)

    # Display Statistics of columns
    df.describe()

    # Handle missing values
    df = df.dropna()  # Drop rows with missing values (or use fillna for imputation)

    # Remove duplicates
    data = data.drop_duplicates()

    # Remove outliers from Profit, Sales, and Discount columns
    # TODO: Create CDF for following columns. You might skip the outlier removal step if you dont' have Normal Distribution.

    # df = remove_outliers(df, 'Profit')
    # df = remove_outliers(df, 'Sales')
    # df = remove_outliers(df, 'Discount')
    

    # Data Type Handling
    # Convert numerical columns to float or integer (coerce invalids to NaN)
    numerical_columns = ['Sales', 'Profit', 'Discount', 'Quantity', 'Shipping_Cost']
    for col in numerical_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        else:
            print(f"Warning: Numerical column '{col}' not found in DataFrame.")

    # Create 'Date' column by combining Order_Date and Time
    if 'Order_Date' in df.columns and 'Time' in df.columns:
        df['Date'] = pd.to_datetime(df['Order_Date'].astype(str) + ' ' + df['Time'].astype(str), errors='coerce')
    else:
        print("Warning: 'Order_Date' or 'Time' column not found. Skipping Date conversion.")

    # Convert Customer_Id to object (string)
    if 'Customer_Id' in df.columns:
        df['Customer_Id'] = df['Customer_Id'].astype('object')
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
    # Convert categorical columns to 'category' dtype
    for col in categorical_columns:
        if col in df.columns:
            df[col] = df[col].astype('category')
        else:
            print(f"Warning: Categorical column '{col}' not found in DataFrame.")

    # Feature Engineering: Extract Month and Quarter, and calculate Profit Margin
    df['Month'] = df['Order_Date'].dt.month
    df['Quarter'] = df['Order_Date'].dt.quarter
    df['Profit_Margin'] = df['Profit'] / df['Sales']



    # Display the first few rows of the cleaned dataset
    print(df.head())

    # Display summary statistics to understand the dataset
    print(df.describe())

    # Display the number of rows in the dataset
    print(f"Number of rows in the dataset: {len(df)}")

    # Descriptive Statistics
    # Calculate overall total profit
    total_profit = df['Profit'].sum()
    # Calculate average profit per order
    average_profit_per_order = df['Profit'].mean()
    print(f"Overall Total Profit: {total_profit}")
    print(f"Average Profit per Order: {average_profit_per_order}")

    # Aggregation & Segmentation
    # Calculate total and average profit per Product_Category
    grouping_dimensions = [
        'Product_Category', 'Product', 'Device_Type', 
        'Customer_Login_type', 'Gender', 'Order_Priority', 'Payment_method'
    ]

    for dimension in grouping_dimensions:
        if dimension in df.columns:
            grouped_data = df.groupby(dimension, observed=True)['Profit'].agg(['sum', 'mean']).reset_index()
            print(f"\nProfit Summary by {dimension}:")
            print(grouped_data)
        else:
            print(f"Warning: Dimension '{dimension}' not found in DataFrame.")

    # Visualisation
    if 'Product_Category' in df.columns:
        profit_by_category = df.groupby('Product_Category', observed=True)['Profit'].sum().sort_values(ascending=False)

        # Plot the bar chart
        plt.figure(figsize=(10, 6))
        profit_by_category.plot(kind='bar', color='skyblue')
        plt.title("Total Profit by Product Category", fontsize=16)
        plt.xlabel("Product Category", fontsize=12)
        plt.ylabel("Total Profit", fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print("Warning: 'Product_Category' column not found in DataFrame.")

    # Set the number of top products to display
    top_n = 10

    # Calculate total profit per Product and sort in descending order
    if 'Product' in df.columns:
        profit_by_product = df.groupby('Product', observed=True)['Profit'].sum().sort_values(ascending=False).head(top_n)

        # Convert to a DataFrame for better readability
        profit_by_product_df = profit_by_product.reset_index()
        profit_by_product_df.columns = ['Product', 'Total Profit']

        # Display the table
        print(f"\nTop {top_n} Products by Total Profit:")
        print(profit_by_product_df)
    else:
        print("Warning: 'Product' column not found in DataFrame.")

    # Device Type
    # Compare total profit by Device_Type using a bar chart
    if 'Device_Type' in df.columns:
        profit_by_device = df.groupby('Device_Type', observed=True)['Profit'].sum().sort_values(ascending=False)

        # Plot the bar chart
        plt.figure(figsize=(8, 5))
        profit_by_device.plot(kind='bar', color='lightgreen')
        plt.title("Total Profit by Device Type", fontsize=16)
        plt.xlabel("Device Type", fontsize=12)
        plt.ylabel("Total Profit", fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print("Warning: 'Device_Type' column not found in DataFrame.")

    # Customer Type
    # Compare total profit by Customer_Login_type using a bar chart
    if 'Customer_Login_type' in df.columns:
        profit_by_login_type = df.groupby('Customer_Login_type', observed=True)['Profit'].sum().sort_values(ascending=False)

        # Plot the bar chart
        plt.figure(figsize=(8, 5))
        profit_by_login_type.plot(kind='bar', color='orange')
        plt.title("Total Profit by Customer Login Type", fontsize=16)
        plt.xlabel("Customer Login Type", fontsize=12)
        plt.ylabel("Total Profit", fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print("Warning: 'Customer_Login_type' column not found in DataFrame.")


# Time Series Analysis

# --- Monthly Profit Line Plot ---

    # Convert numeric month to abbreviated name
    # Calculate monthly profit
    if 'Month' in df.columns and 'Profit' in df.columns:
        monthly_profit = df.groupby('Month', observed=True)['Profit'].sum().reset_index()
        monthly_profit['Month_Name'] = monthly_profit['Month'].apply(lambda x: calendar.month_abbr[x])
        monthly_profit['Month_Name'] = pd.Categorical(
            monthly_profit['Month_Name'],
            categories=list(calendar.month_abbr)[1:],  # Skip empty string at index 0
            ordered=True
        )
        monthly_profit = monthly_profit.sort_values('Month_Name')

        plt.figure(figsize=(12, 5))
        sns.lineplot(data=monthly_profit, x='Month_Name', y='Profit', marker='o', linewidth=2, color='royalblue')
        plt.title('Total Profit by Month')
        plt.xlabel('Month')
        plt.ylabel('Total Profit')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("Warning: 'Month' or 'Profit' column not found in DataFrame.")

        # --- Quarterly Profit Line Plot ---
        if 'Quarter' in df.columns and 'Profit' in df.columns:
            quarterly_profit = df.groupby('Quarter', observed=True)['Profit'].sum().reset_index()
            quarter_labels = ['Q1', 'Q2', 'Q3', 'Q4']
            quarterly_profit['Quarter_Label'] = quarterly_profit['Quarter'].apply(lambda x: quarter_labels[x - 1])
            quarterly_profit = quarterly_profit.sort_values('Quarter')

            plt.figure(figsize=(8, 5))
            sns.lineplot(data=quarterly_profit, x='Quarter_Label', y='Profit', marker='o', linewidth=2, color='darkgreen')
            plt.title('Total Profit by Quarter')
            plt.xlabel('Quarter')
            plt.ylabel('Total Profit')
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        else:
            print("Warning: 'Quarter' or 'Profit' column not found in DataFrame.")

        plt.figure(figsize=(8, 5))
        sns.lineplot(data=quarterly_profit, x='Quarter_Label', y='sum', marker='o', linewidth=2, color='darkgreen')
    plt.title('Total Profit by Quarter')
    plt.xlabel('Quarter')
    plt.ylabel('Total Profit')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Correlation Analysis
    # List of numerical variables to analyze
    numerical_variables = ['Sales', 'Quantity', 'Discount', 'Shipping_cost']

    # Calculate and display correlation coefficients
    print("\nCorrelation Coefficients with Profit:")
    for variable in numerical_variables:
        if variable in df.columns:
            correlation = df['Profit'].corr(df[variable])
            print(f"Correlation between Profit and {variable}: {correlation:.2f}")
        else:
            print(f"Warning: Numerical variable '{variable}' not found in DataFrame.")

    # Visualize relationships using scatter plots
    for variable in numerical_variables:
        if variable in df.columns:
            plt.figure(figsize=(6, 4))
            sns.scatterplot(x=df[variable], y=df['Profit'])
            plt.title(f"Profit vs {variable}")
            plt.xlabel(variable)
            plt.ylabel("Profit")
            plt.show()

if "__name__" == "__main__":
    main()
    # Main function to run the script
    pass