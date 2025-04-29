
import streamlit as st
import pandas as pd
from csv_loader import load_transactions
from categorizer import categorize_transactions
from suggestion_engine import generate_savings_suggestions
from collections import defaultdict

st.set_page_config(page_title="Expense Optimizer AI", page_icon="💵")

st.title("💵 Personal Expense Optimizer AI")
st.write("Upload your bank transactions and get smart savings suggestions!")

uploaded_file = st.file_uploader("Upload your transactions CSV", type=["csv"])

if uploaded_file:
    transactions = load_transactions(uploaded_file)
    categorized = categorize_transactions(transactions)
    suggestions = generate_savings_suggestions(categorized)

    # Display transactions
    st.subheader("📄 Transactions")
    df = pd.DataFrame(categorized)
    st.dataframe(df)

    # Category Spend Summary
    st.subheader("📊 Spending by Category")
    category_totals = defaultdict(float)
    for tx in categorized:
        category_totals[tx['category']] += tx['amount']
    
    if category_totals:
        chart_data = pd.DataFrame({
            'Category': list(category_totals.keys()),
            'Total Spent': list(category_totals.values())
        })
        st.bar_chart(chart_data.set_index('Category'))
    
    # Show Suggestions
    st.subheader("💡 Savings Suggestions")
    if suggestions:
        for sug in suggestions:
            st.success(f"💡 {sug['text']} (Potential Savings: ${sug['potential_savings']:.2f})")
    else:
        st.info("No savings suggestions found. Good job! 🎉")
else:
    st.info("Please upload a CSV file to proceed.")
