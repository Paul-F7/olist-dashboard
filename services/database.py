def get_connection():
    return sqlite3.connect('../data/olist.db')

def close_connection(conn):
    if conn:
        conn.close()
    return print('Connection closed')