import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Online Food Delivery Dashboard",
    page_icon="🍔",
    layout="wide"
)

st.title("Online Food Delivery Analysis")
st.subheader("Data-Driven Business Insights")


@st.cache_data
def load_data():
    return pd.read_csv("ONINE_FOOD_DELIVERY_ANALYSIS.csv")


df = load_data()

# Convert numeric columns safely
for column in ["Final_Amount", "Delivery_Time_Min", "Delivery_Rating",
               "Restaurant_Rating", "Rating", "Profit_Margin"]:
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

# Find a date column only if it exists in the dataset
possible_date_columns = [
    "Order_Date", "OrderDate", "Date", "Order_Timestamp",
    "Order_DateTime", "Order_Datetime"
]
date_column = next((col for col in possible_date_columns if col in df.columns), None)

if date_column:
    df[date_column] = pd.to_datetime(df[date_column], errors="coerce")

# -------------------- FILTERS --------------------
st.sidebar.header("Dashboard Filters")

filtered_df = df.copy()

if "City" in filtered_df.columns:
    city_options = ["All"] + sorted(
        filtered_df["City"].dropna().astype(str).unique().tolist()
    )
    selected_city = st.sidebar.selectbox("Select City", city_options)
    if selected_city != "All":
        filtered_df = filtered_df[
            filtered_df["City"].astype(str) == selected_city
        ]

if "Cuisine_Type" in filtered_df.columns:
    cuisine_options = ["All"] + sorted(
        filtered_df["Cuisine_Type"].dropna().astype(str).unique().tolist()
    )
    selected_cuisine = st.sidebar.selectbox("Select Cuisine", cuisine_options)
    if selected_cuisine != "All":
        filtered_df = filtered_df[
            filtered_df["Cuisine_Type"].astype(str) == selected_cuisine
        ]

if "Order_Status" in filtered_df.columns:
    status_options = ["All"] + sorted(
        filtered_df["Order_Status"].dropna().astype(str).unique().tolist()
    )
    selected_status = st.sidebar.selectbox("Select Order Status", status_options)
    if selected_status != "All":
        filtered_df = filtered_df[
            filtered_df["Order_Status"].astype(str) == selected_status
        ]

if date_column and filtered_df[date_column].notna().any():
    valid_dates = filtered_df[date_column].dropna()
    min_date = valid_dates.min().date()
    max_date = valid_dates.max().date()
    selected_dates = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    if isinstance(selected_dates, tuple) and len(selected_dates) == 2:
        start_date, end_date = selected_dates
        filtered_df = filtered_df[
            filtered_df[date_column].dt.date.between(start_date, end_date)
        ]

st.caption(f"Showing {len(filtered_df):,} orders after applying filters.")

# -------------------- KPI CALCULATIONS --------------------
total_orders = len(filtered_df)

if "Order_Status" in filtered_df.columns:
    delivered_df = filtered_df[
        filtered_df["Order_Status"].astype(str).str.lower() == "delivered"
    ]
    cancelled = (
        filtered_df["Order_Status"].astype(str).str.lower() == "cancelled"
    ).sum()
else:
    delivered_df = filtered_df.copy()
    cancelled = 0

delivered = len(delivered_df)
cancel_rate = (cancelled / total_orders * 100) if total_orders else 0

revenue = 0
average_order_value = 0
if "Final_Amount" in delivered_df.columns:
    delivered_amounts = delivered_df["Final_Amount"].dropna()
    revenue = delivered_amounts.sum()
    average_order_value = delivered_amounts.mean() if not delivered_amounts.empty else 0

average_delivery_time = (
    pd.to_numeric(filtered_df["Delivery_Time_Min"], errors="coerce").mean()
    if "Delivery_Time_Min" in filtered_df.columns else None
)

# Prefer an actual delivery-rating column. Do not label restaurant rating as delivery rating.
rating_column = None
rating_label = "Average Delivery Rating"
if "Delivery_Rating" in filtered_df.columns:
    rating_column = "Delivery_Rating"
elif "Restaurant_Rating" in filtered_df.columns:
    rating_column = "Restaurant_Rating"
    rating_label = "Average Restaurant Rating"
elif "Rating" in filtered_df.columns:
    rating_column = "Rating"
    rating_label = "Average Rating"

average_rating = (
    pd.to_numeric(filtered_df[rating_column], errors="coerce").mean()
    if rating_column else None
)

average_profit_margin = (
    pd.to_numeric(filtered_df["Profit_Margin"], errors="coerce").mean()
    if "Profit_Margin" in filtered_df.columns else None
)

# -------------------- KPI DISPLAY --------------------
k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Orders", f"{total_orders:,}")
k2.metric("Total Revenue", f"{revenue:,.2f}")
k3.metric("Average Order Value", f"{average_order_value:,.2f}")
k4.metric("Average Delivery Time",
          f"{average_delivery_time:.1f} minutes" if pd.notna(average_delivery_time)
          else "N/A")

k5, k6, k7 = st.columns(3)
k5.metric("Cancellation Rate", f"{cancel_rate:.2f}%")
k6.metric(rating_label, f"{average_rating:.2f}" if pd.notna(average_rating)
          else "Column not available")
k7.metric("Average Profit Margin",
          f"{average_profit_margin:.2f}" if pd.notna(average_profit_margin)
          else "Column not available")

st.divider()

# -------------------- EXISTING CHARTS --------------------
if "City" in filtered_df.columns:
    st.subheader("City-wise Orders")
    city_counts = filtered_df["City"].fillna("Unknown").value_counts()
    st.bar_chart(city_counts)

if "Cuisine_Type" in filtered_df.columns:
    st.subheader("Cuisine-wise Orders")
    cuisine_counts = filtered_df["Cuisine_Type"].fillna("Unknown").value_counts()
    st.bar_chart(cuisine_counts)

if "Order_Status" in filtered_df.columns:
    st.subheader("Order Status")
    st.bar_chart(filtered_df["Order_Status"].fillna("Unknown").value_counts())

if "Order_Status" in filtered_df.columns and "Cancellation_Reason" in filtered_df.columns:
    st.subheader("Cancellation Reasons")
    cancelled_df = filtered_df[
        filtered_df["Order_Status"].astype(str).str.lower() == "cancelled"
    ]
    reasons = cancelled_df["Cancellation_Reason"].fillna("Unknown").value_counts()
    st.bar_chart(reasons)

if "Delivery_Time_Min" in filtered_df.columns:
    st.subheader("Delivery Time Analysis")
    delivery_time = pd.to_numeric(
        filtered_df["Delivery_Time_Min"], errors="coerce"
    ).dropna()

    if not delivery_time.empty:
        st.bar_chart(delivery_time.value_counts().sort_index())

# -------------------- MONTHLY REVENUE --------------------
if date_column and "Final_Amount" in delivered_df.columns:
    monthly_df = delivered_df.dropna(subset=[date_column, "Final_Amount"]).copy()
    if not monthly_df.empty:
        monthly_df["Month"] = monthly_df[date_column].dt.to_period("M").astype(str)
        monthly_revenue = monthly_df.groupby("Month")["Final_Amount"].sum()
        st.subheader("Monthly Revenue Trend")
        st.line_chart(monthly_revenue)
else:
    st.info(
        "Monthly Revenue Trend is not displayed because a recognized date column "
        "was not found in the dataset."
    )

st.caption("Online Food Delivery Analysis | Project Dashboard")
