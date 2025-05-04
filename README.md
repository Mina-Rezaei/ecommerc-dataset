# ecommerc-dataset
# 1. Introduction

## Problem Statement: 
### The goal of this analysis is to identify the primary sources of profit within the provided e-commerce dataset covering one year of sales in America. We aim to answer the question: 'Where is the most profit generated?' to help stakeholders make informed decisions regarding resource allocation, marketing focus, and strategic planning.

## Business Context: 
### Understanding profit drivers is crucial for optimising business operations, improving marketing ROI, managing inventory effectively, and ultimately increasing overall profitability.

# 2. Data Source

## Origin: 
### The data used for this analysis is the 'ecommerce-dataset' sourced from Kaggle.

## Scope: 
### It contains transaction details for one year of online purchases within America.

## Key Columns: 
### Relevant columns for this profit analysis include Profit, Product_Category, Product, Sales, Quantity, Discount, Shipping_cost, Customer_id, Gender, Device_Type, Customer_Login_Type, Order_Priority, Payment_method, and Order_Date.

## Quality & Limitations:
### - The dataset provides a snapshot of one year, so findings might not capture longer-term trends or seasonality beyond that period.
### - Geographic scope is limited to 'America' (the specifics of which region 'America' refers to - US, North America, etc. - might be a limitation if not clearly defined in the metadata).
### - Data quality needs assessment. Initial checks has been performed for missing values, outliers, and inconsistencies (e.g., negative profit, unreasonable discounts) which could impact the analysis.
### - The granularity of Product might be very high, potentially requiring aggregation to the Product_Category level for clearer insights.

# 3. Methodology

## Tools: 
### The analysis was conducted using Python with Pandas library for data manipulation and Matplotlib/Seaborn for visualisation.

## Data Cleaning & Preparation:
### - Initial steps involved loading the dataset and assessing its structure and data types.
### - Handled missing values in key columns. 
### - Removed Duplicates
### - Convert columns to appropriate data types e.g. createed 'Date' column by combining Order_Date and Time
### - Remove outliers from Profit, Sales, and Discount columns using IQR method
### - Convert numerical columns ('Sales', 'Profit', 'Discount', 'Quantity', 'Shipping_Cost') to float or integer (coerce invalids to NaN)
### - Convert categorical columns ('Gender', 'Device_Type', 'Customer_Login_type', 'Product_Category', 'Order_Priority', 'Payment_method') to 'category' dtype
### - Feature Engineering: Extracted new features such as 'Month' or 'Quarter' from Order_Date to analyse time trends, and calculating 'Profit Margin'.


## Analysis Techniques:
### - Descriptive Statistics: Calculated overall total profit and average profit per order.
Overall Profit Metrics:
Total Sales: $7,813,411.00
Total Profit: $3,611,186.60
Average Profit Margin: 42.53%

###  - Aggregation & Segmentation: Grouped the data by various dimensions (Product_Category, Product, Device_Type, Customer_Login_Type, Gender, Order_Priority, Payment_method) and calculated the sum and/or average Profit for each segment.

### - Time Series Analysis: Aggregated profit by month or quarter (derived from Order_Date) to identify any temporal patterns or seasonality in profitability.
#### - Monthly Profit: Profit shows a gradual upward trend from January to November, peaking in November ($406,808.7), followed closely by May and July.

#### - The average monthly profit stays fairly consistent (~$70 per transaction), but total monthly profit varies, possibly reflecting differences in transaction volume.

#### - There may be a seasonal pattern with increased profitability in Q2 to Q4, suggesting stronger performance in mid to late year.

#### - Quarterly Profit:
#### - Profit increases steadily across quarters, with Q4 being the most profitable (total profit: $1,103,875.7).

Profit Summary by Month:
    Month       sum       mean
0       1  174573.6  69.302739
1       2  153288.2  69.486945
2       3  200936.8  69.312453
3       4  277646.2  71.301027
4       5  379205.8  70.028772
5       6  298246.1  71.384897
6       7  374242.9  70.346410
7       8  306771.5  70.167315
8       9  341558.1  70.409833
9      10  342228.5  70.057011
10     11  406808.7  71.633862
11     12  354838.5  70.070794

Profit Summary by Quarter:
   Quarter        sum       mean
0        1   528798.6  69.359732
1        2   955098.1  70.816201
2        3  1022572.5  70.313725
3        4  1103875.7  70.634483

### - Correlation Analysis: Investigated relationships between Profit and other numerical variables like Sales, Quantity, Discount, and Shipping_cost to understand factors influencing profitability.

# 4. Findings

## Overall Profit: 
### The total profit generated over the year was $3,611,186.60
Total Sales: $7,813,411
Total Profit: $3,611,186.60
Average Profit Margin: 42.53 %

## Profit by Product Category:
### - Total profit per Product_Category, sorted from highest to lowest.
![Alt text](/Users/mina.rezaei/Desktop/Repository/ecommerce-profit/ecommerc-dataset/profit_per_product_cat.jpg)
### - Fashion is by far the most profitable category, accounting for $2,072,624 in profit—57.4 % of total profit—on 55.6 % of total sales. It out‑performs the next category (Home & Furniture) by over $1.19 million in absolute profit.
Product Category	Total Profit	Profit Share	Sales Share
Fashion	$2,072,624	57.39 %	55.62 %
Home & Furniture	$880,059	24.37 %	25.29 %
Auto & Accessories	$484,313	13.41 %	14.04 %
Electronic	$174,191	4.82 %	5.05 %

## High-Profit Products: Within the top categories, specific products like [T - Shirts, Titak watch] stand out as major profit contributors.

Top 10 Products by Total Profit:
         Product  Total Profit
0     T - Shirts      340720.6
1    Titak watch      296718.2
2  Running Shoes      289097.6
3          Jeans      276856.3
4   Formal Shoes      265350.7
5         Shirts      230078.3
6         Towels      196828.2
7    Sofa Covers      178920.5
8     Bed Sheets      172262.9
9   Fossil Watch      151271.7
### - Device Type: Comparing Device_Type, we found that purchases made via Web generate higher total profit compared to Moblie.
![Alt text](/Users/mina.rezaei/Desktop/Repository/ecommerce-profit/ecommerc-dataset/profit_per_device_type.jpg)

### - Customer Type: Analysis of Customer_Login_type shows that Members contribute significantly more to overall profit. 
![Alt text](/Users/mina.rezaei/Desktop/Repository/ecommerce-profit/ecommerc-dataset/profit_per_customer_login_type.jpg)

### - Profitability Drivers: (Use Scatter Plots or Bar Charts)
#### - There is a strong positive relationship between Sales and Profit (correlation: 0.92). While higher sales generally lead to higher profit, the scatter plot may show some dispersion, possibly due to variable costs or discounting.
(Show scatter plot: Profit vs Sales)

#### - The Discount rate shows no significant correlation with Profit (correlation: -0.00). This suggests that discounting practices are either minimal or not directly affecting profitability on average.
(Show scatter plot: Profit vs Discount, optionally colored by category)

#### - Interestingly, there is a perfect positive correlation between Shipping Cost and Profit (correlation: 1.00), which may indicate a calculated or derived relationship — e.g., profit being computed based on shipping cost in the dataset.
(Show scatter plot: Profit vs Shipping Cost)

#### - The relationship between Quantity and Profit is weakly negative (correlation: -0.12), suggesting that selling more units does not always translate into higher profits and could be due to high-volume, low-margin products.


# 5. Recommendations

## - Focus on High-Profit Areas: Allocate marketing budget and inventory investment towards the top profit-generating Product_Category ([List them again]). Explore opportunities for cross-selling or up-selling within these categories.

## - Address Low-Profit Areas: Investigate the low profitability of [List bottom categories/products]. Analyse their cost structure, pricing strategy, and discount levels. Consider strategic repricing, cost reduction, or even SKU rationalization (discontinuation) if they consistently generate losses.

## - Optimise Channel Strategy: Given the profitability associated with [Web/Mobile] users, ensure a seamless user experience on this platform. If one channel lags, investigate potential friction points.

## - Leverage Customer Type: Since [Members/Guests] are more profitable, develop strategies to encourage sign-ups or enhance loyalty programs to increase member engagement and retention.

## - Review Discount Policy: Re-evaluate the discounting strategy, particularly for categories where high discounts significantly erode profit margins. Implement smarter, targeted promotions instead of broad, deep discounts.

## - Manage Seasonality: Plan promotional activities and inventory levels according to the observed seasonal profit trends ([mention peak/low periods]) to maximize returns during peak times and mitigate losses during off-peak periods.

# 6. Conclusion

## - In conclusion, this analysis pinpointed where the most profit is found within the business's e-commerce operations over the past year. The primary drivers are clearly [mention top product categories] and potentially influenced by [mention key factor like customer type or device].

## - By focusing resources on the most profitable segments, addressing areas of low profitability, and refining strategies around customer types, channels, and promotions, the business can make data-driven decisions to enhance overall profitability.

## - These insights provide a clear roadmap for strategic adjustments aimed at boosting the bottom line.