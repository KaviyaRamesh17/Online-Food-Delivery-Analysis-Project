# Online Food Delivery Analysis -- Data-Driven Business Insights

## 1. Project Introduction

Online food delivery platforms generate large amounts of data every day.
Analyzing this data helps businesses understand customer behaviour,
delivery performance, revenue, restaurant performance, and order
cancellations.

This project focuses on analyzing online food delivery data and
generating meaningful business insights using Python, SQL, and data
visualization.

## 2. Project Objective

-   Analyze customer ordering patterns.
-   Identify high-revenue cities and cuisines.
-   Understand weekday and weekend order trends.
-   Analyze delivery time and delivery delays.
-   Identify major reasons for order cancellations.
-   Understand business performance using KPIs.
-   Create an interactive dashboard for business insights.

## 3. Dataset Description

The dataset contains **100,000 rows and 25 columns** related to online
food delivery orders.

The dataset includes information such as:

-   Order ID
-   Customer Age
-   City
-   Cuisine Type
-   Delivery Time
-   Final Amount
-   Order Status
-   Cancellation Reason
-   Profit Margin

## 4. Technologies Used

  Technology   Purpose
  ------------ -------------------------------------
  Python       Data analysis
  Pandas       Data manipulation
  NumPy        Numerical operations
  Matplotlib   Data visualization
  Seaborn      Statistical visualization
  MySQL        Database management and SQL queries
  Streamlit    Interactive dashboard

## 5. Data Cleaning and Preprocessing

The following cleaning activities were performed:

-   Checked missing values.
-   Checked duplicate Order IDs.
-   Handled missing customer age values using median.
-   Replaced blank cancellation reasons with Unknown for cancelled
    orders.
-   Corrected negative Final Amount values.
-   Checked invalid ratings and profit margin values.
-   Prepared the dataset for analysis.

**Why is data cleaning important?**

Data cleaning improves data quality and helps produce more reliable
analysis results.

## 6. Exploratory Data Analysis (EDA)

The following analyses were performed:

1.  Order and customer distribution analysis.
2.  City-wise and cuisine-wise order analysis.
3.  Weekday versus weekend order analysis.
4.  Distance versus delivery delay analysis.
5.  Cancellation reason analysis.
6.  Correlation analysis between numerical columns.

## 7. Key Business Insights

-   Total Orders: **100,000**
-   Delivered Orders: **84,964**
-   Cancelled Orders: **15,036**
-   Cancellation Rate: **15.04%**
-   Average Delivery Time: **127.5 minutes**

### City-wise Orders

-   Hyderabad: 16,884
-   Bangalore: 16,732
-   Delhi: 16,695
-   Mumbai: 16,493
-   Chennai: 16,470

### Cuisine-wise Orders

-   Indian: 16,685
-   Arabian: 16,658
-   Chinese: 16,651
-   Mexican: 16,602
-   Italian: 16,519

These insights help understand customer demand and business performance.

## 8. SQL Analysis

MySQL was used to store and analyze the food delivery dataset.

SQL concepts used include:

-   SELECT
-   FROM
-   WHERE
-   GROUP BY
-   ORDER BY
-   COUNT()
-   SUM()
-   AVG()

These queries help filter, group, summarize, and analyze order
information.

## 9. Streamlit Dashboard

An interactive dashboard was developed using Streamlit.

### Dashboard KPIs

-   Total Orders
-   Total Revenue
-   Average Order Value
-   Average Delivery Time
-   Cancellation Rate
-   Average Delivery Rating
-   Average Profit Margin

### Dashboard Filters

-   City
-   Cuisine
-   Order Status
-   Date Range

### Dashboard Visualizations

-   City-wise Orders
-   Cuisine-wise Orders
-   Order Status Analysis
-   Cancellation Reasons
-   Delivery Time Analysis
-   Monthly Revenue Trend

The dashboard helps users explore the data interactively and understand
important business insights.

## 10. Conclusion

The Online Food Delivery Analysis project helped identify customer
ordering patterns, city-wise demand, cuisine preferences, delivery
performance, and cancellation trends.

By using Python, SQL, and Streamlit, the project converts raw food
delivery data into meaningful business insights.

This analysis can help food delivery businesses improve customer
satisfaction, delivery efficiency, and business performance.
