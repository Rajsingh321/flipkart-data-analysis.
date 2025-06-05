import pandas as pd
import streamlit as st
from PIL import Image
import os




st.title("Flipkart Product Analysis")
data = pd.read_csv("mega 1 website/flipkart_products_20250405.csv")

st.subheader("Data preview")
st.write(data.head(10))

st.subheader("Data Description")
st.table(data.describe())
insights ="""Product-Wise Sales:
Certain products (e.g., Canon ink, Fellowes folders) contribute disproportionately to total sales—top 3 products dominate the chart.

Sub-Category Analysis:
Phones, Chairs, and Storage drive the highest sales within sub-categories. Copiers and Bookcases underperform.

Profitability Gaps:
While some products like Canon ink are both high in sales and profits, others generate sales but contribute little or even negative profit.

Category Performance:
Technology leads in total sales, followed by Furniture and Office Supplies. However, Office Supplies show more stable profits.

Profit Margin Breakdown:
A large chunk of profit is generated from Technology and Office Supplies, while Furniture has thinner margins overall.

High Loss Products:
Several products show extremely negative profit margins (up to -275%), signaling urgent attention for pricing or promotional review.

Discount Sensitivity:
Profit drastically drops at discounts above 0.3. There's a sweet spot where discounting drives sales without killing margins.

Discount by Category:
Office Supplies benefit the most from discounts, but too much discounting wipes out margins.

Time-Series Trends:
Monthly sales peak around November (likely due to holidays), while yearly trends show steady upward growth from 2015 onward.

Profit Drivers:
Copiers and Accessories are top contributors to profit, while some product lines consistently lose money.

"""
st.subheader("📜Insights")
st.write(insights)


try:
    img = Image.open("mega 1 website/page 1.png")
    st.image(img, caption="📄 Page 1", use_column_width=True)
except FileNotFoundError:
    st.warning(" ")

try:
    img = Image.open("mega 1 website/page 2.png")
    st.image(img, caption="📄 Page 2", use_column_width=True)
except FileNotFoundError:
    st.warning(" ")

try:
    img = Image.open("mega 1 website/page 3.png")
    st.image(img, caption="📄 Page 3", use_column_width=True)
except FileNotFoundError:
    st.warning(" ")

try:
    img = Image.open("mega 1 website/page 4.png")
    st.image(img, caption="📄 Page 4", use_column_width=True)
except FileNotFoundError:
    st.warning(" ")
