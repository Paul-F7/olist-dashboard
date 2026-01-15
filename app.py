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

