import pandas as pd
import sqlite3
from database import get_connection, close_connection

#Exectures sql file and returns as DataFrame
def execute_sql(filename):
    conn = get_connection()
    sql_path = f'sql/{filename}'

    with open(sql_path, 'r') as f:
        query = f.read()
    
    df = pd.read_sql(query, conn)
    close_connection(conn)
    return df


def get_revenue_over_time():
    return execute_sql('revenue_over_time.sql')

def get_top_categories():
    return execute_sql('top_categories.sql')

def get_delivery_performance():
    return execute_sql('delivery_performance.sql')

def get_customer_geography():
    return execute_sql('customer_geography.sql')
