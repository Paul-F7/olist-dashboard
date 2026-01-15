import streamlit as st
import pandas as pd
from services.queries import (
    get_revenue_over_time,
    get_top_categories,
    get_delivery_performance,
    get_customer_geography
)
from services.visualizations import (
    create_revenue_chart,
    create_orders_chart,
    create_categories_chart,
    create_delivery_chart,
    create_customer_distribution_chart,
    create_revenue_distribution
)

# Page config
st.set_page_config(
    page_title="Olist Dashboard",
    page_icon="📊",
    layout="wide"
)

# Header
st.title("Olist E-Commerce Dashboard")
st.markdown("Analyzing 100k+ orders from Brazilian marketplace")
st.divider()

# Load data
revenue_df = get_revenue_over_time()
categories_df = get_top_categories()
delivery_df = get_delivery_performance()
geo_df = get_customer_geography()


# Prepare data
revenue_df['date'] = pd.to_datetime(revenue_df['date'])
state_summary = geo_df.groupby('customer_state').agg({
    'customers': 'sum',
    'orders': 'sum'
}).reset_index()
state_summary = state_summary.sort_values('customers', ascending=False)

# Overview Metrics 
st.header('Overview')

col1, col2, col3, col4 = st.columns(4)

total_revenue = revenue_df['revenue'].sum()
total_orders = revenue_df['orders'].sum()
avg_order_value = total_revenue / total_orders
total_categories = len(categories_df)

with col1:
    st.metric("Total Revenue", f"R$ {total_revenue:,.0f}")
with col2:
    st.metric("Total Orders", f"{total_orders:,}")
with col3:
    st.metric("Avg Order Value", f"R$ {avg_order_value:.2f}")
with col4:
    st.metric("Product Categories", f"{total_categories}")

st.divider()

# Revenue Trends
st.header("Revenue Trends")

col1, col2 = st.columns(2)

with col1:
    fig_revenue = create_revenue_chart(revenue_df)
    st.pyplot(fig_revenue)

with col2:
    fig_orders = create_orders_chart(revenue_df)
    st.pyplot(fig_orders)

st.divider()

# Top Categories
st.header(" Top Product Categories")

col1, col2 = st.columns([2, 1])

with col1:
    fig_categories = create_categories_chart(categories_df, top_n=10)
    st.pyplot(fig_categories)

with col2:
    fig_pie = create_revenue_distribution(categories_df)
    st.pyplot(fig_pie)

with st.expander("📋 View Full Category Data"):
    st.dataframe(
        categories_df.style.format({
            'revenue': 'R$ {:,.2f}',
            'sales': '{:,}'
        }),
        use_container_width=True
    )

st.divider()

# Delivery Preformance
st.header("Delivery Performance")

col1, col2 = st.columns([2, 1])

with col1:
    fig_delivery = create_delivery_chart(delivery_df, top_n=10)
    st.pyplot(fig_delivery)

with col2:
    best_state = delivery_df.loc[delivery_df['avg_delivery_days'].idxmin()]
    worst_state = delivery_df.loc[delivery_df['avg_delivery_days'].idxmax()]
    avg_delivery = delivery_df['avg_delivery_days'].mean()
    
    st.markdown("### Delivery Insights")
    st.success(f"**Fastest:** {best_state['customer_state']} - {best_state['avg_delivery_days']:.1f} days")
    st.error(f"**Slowest:** {worst_state['customer_state']} - {worst_state['avg_delivery_days']:.1f} days")
    st.info(f"**National Average:** {avg_delivery:.1f} days")

st.divider()


# Geographic Distribution
st.header("Customer Distribution")

fig_geo = create_customer_distribution_chart(state_summary, top_n=15)
st.pyplot(fig_geo)

with st.expander("View Top Cities"):
    st.dataframe(
        geo_df.head(20).style.format({
            'customers': '{:,}',
            'orders': '{:,}'
        }),
        use_container_width=True
    )

# Footer
st.divider()
st.markdown("*Data source: Olist Brazilian E-Commerce Dataset | Built with Pandas, SQLite, Matplotlib, Streamlit*")