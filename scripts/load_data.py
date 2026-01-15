import pandas as pd
import sqlite3

conn = sqlite3.connect('olist.db')

tables = ['customers', 'geolocation', 'order_items', 'order_payments', 'order_reviews', 'orders', 'products', 'sellers']

for table in tables:
    df = pd.read_csv(f'../data/raw/olist_{table}_dataset.csv')
    df.to_sql(table, conn, if_exists='replace', index=False)
    print(f'Loaded table: {table}')
df = pd.read_csv(f'../data/raw/product_category_name_translation.csv')

df.to_sql('translation', conn, if_exists='replace', index=False)
print("All done")