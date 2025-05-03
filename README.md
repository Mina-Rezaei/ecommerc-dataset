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

                         Order_Date         Aging         Sales  \
count                          51282  51282.000000  51282.000000   
mean   2018-07-23 11:35:56.124955904      5.255187    152.337350   
min              2018-01-01 00:00:00      1.000000     33.000000   
25%              2018-05-07 00:00:00      3.000000     85.000000   
50%              2018-07-28 00:00:00      5.000000    133.000000   
75%              2018-10-17 00:00:00      8.000000    218.000000   
max              2018-12-30 00:00:00     10.500000    250.000000   
std                              NaN      2.960073     66.492468   

           Quantity      Discount        Profit  Shipping_Cost  \
count  51282.000000  51282.000000  51282.000000   51282.000000   
mean       2.502964      0.303838     70.401796       7.041166   
min        1.000000      0.100000      0.500000       0.100000   
25%        1.000000      0.200000     24.900000       2.500000   
50%        2.000000      0.300000     59.900000       6.000000   
75%        4.000000      0.400000    118.400000      11.800000   
max        5.000000      0.500000    167.500000      16.800000   
std        1.511834      0.131025     48.728131       4.871685   

                                Date         Month       Quarter  \
count                          51282  51282.000000  51282.000000   
mean   2018-07-24 02:52:24.765083136      7.240533      2.744413   
min              2018-01-01 00:03:33      1.000000      1.000000   
25%       2018-05-07 19:45:01.500000      5.000000      2.000000   
50%              2018-07-28 09:32:20      7.000000      3.000000   
75%    2018-10-17 17:26:34.249999872     10.000000      4.000000   
max              2018-12-30 23:52:42     12.000000      4.000000   
std                              NaN      3.230997      1.047431   

       Profit_Margin  
count   51282.000000  
mean        0.425263  
min         0.006024  
25%         0.250746  
50%         0.442857  
75%         0.562946  
max         1.000000  
std         0.200703  
Number of rows in the dataset: 51282

## Analysis Techniques:
### - Descriptive Statistics: Calculated overall total profit and average profit per order.
Overall Total Profit: 3610344.9000000004
Average Profit per Order: 70.40179595179596

###  - Aggregation & Segmentation: Grouped the data by various dimensions (Product_Category, Product, Device_Type, Customer_Login_Type, Gender, Order_Priority, Payment_method) and calculated the sum and/or average Profit for each segment.
Profit Summary by Product_Category:
     Product_Category        sum       mean
0  Auto & Accessories   483471.5  64.488662
1          Electronic   174190.6  64.491151
2             Fashion  2072623.9  80.816654
3    Home & Furniture   880058.9  57.006018

Profit Summary by Product:
                   Product       sum        mean
0             Apple Laptop   33025.0  149.434389
1               Bed Sheets  172262.9  111.786437
2                     Beds   53592.5   34.755188
3               Bike Tyres   26767.2   32.445091
4          Car & Bike Care   22700.3   27.482203
5          Car Body Covers   21629.9   26.186320
6                  Car Mat   20782.8   25.191273
7        Car Media Players   39933.8   48.404606
8   Car Pillow & Neck Rest  107735.8  130.115700
9          Car Seat Covers   20006.9   24.192140
10            Car Speakers   92034.8  111.557333
11            Casula Shoes   71894.5   30.842771
12                Curtains   23881.3   15.497274
13         Dinner Crockery   64287.5   41.052043
14          Dinning Tables   43326.0   28.097276
15                    Fans   12047.7   54.514480
16            Formal Shoes  265350.7  113.835564
17            Fossil Watch  151271.7   64.867796
18                    Iron   26833.2  121.417195
19                   Jeans  276856.3  118.720540
20                Keyboard    3292.4   14.897738
21                     LCD    6197.2   27.666071
22                     LED   20910.0   93.348214
23            Mixer/Juicer    5033.3   22.470089
24                   Mouse    4632.8   20.962896
25           Running Shoes  289097.6  124.022994
26          Samsung Mobile   26568.6  120.219910
27                  Shirts  230078.3   98.661364
28               Shoe Rack   50886.5   33.000324
29                Sneakers   66820.7   28.666109
30             Sofa Covers  178920.5  116.257635
31                   Sofas   46283.9   30.015499
32                Speakers    9909.2   37.966284
33             Sports Wear   38984.0   16.724153
34                   Suits   44831.3   19.224400
35              T - Shirts  340720.6  146.106604
36                  Tablet   22312.7  100.962443
37             Titak watch  296718.2  127.292235
38                  Towels  196828.2  127.727579
39                    Tyre  131880.0  148.179775
40               Umbrellas   49789.6   32.288975
41                   Watch    3428.5   15.513575

Profit Summary by Device_Type:
  Device_Type        sum       mean
0      Mobile   262289.7  71.703034
1         Web  3348055.2  70.301848

Profit Summary by Customer_Login_type:
  Customer_Login_type        sum       mean
0        First SignUp    11528.5  66.638728
1               Guest   143513.7  72.008881
2              Member  3453135.3  70.344381
3                New      2167.4  80.274074

Profit Summary by Gender:
   Gender        sum       mean
0  Female  1620200.4  69.987058
1    Male  1990144.5  70.743086

Profit Summary by Order_Priority:
  Order_Priority        sum       mean
0       Critical   283734.2  72.233758
1           High  1112790.2  71.802181
2            Low   169104.1  69.762417
3         Medium  2044716.4  69.472560

Profit Summary by Payment_method:
  Payment_method        sum       mean
0    credit_card  2692363.4  70.608256
1     debit_card    50433.0  68.803547
2       e_wallet   194710.3  69.813661
3    money_order   672829.7  69.882603
4    not_defined        8.5   8.500000

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
### The total profit generated over the year was $3,610,344.9

## Profit by Product Category:
### - Total profit per Product_Category, sorted from highest to lowest.
![Alt text](/Users/mina.rezaei/Desktop/Repository/ecommerce-profit/ecommerc-dataset/profit_per_product_cat.jpg)
### - The analysis reveals that the most significant portion of profit comes from Fashion. Conversely, Electronics contribute the least profit, or potentially generate losses.

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