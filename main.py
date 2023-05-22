import psycopg2

def get_customer_info(name):
    conn = psycopg2.connect(
        dbname='mydatabase', 
        user='myuser', 
        password='mypassword', 
        host='localhost',
        port="5432"
    )
    cur = conn.cursor()
    query = "SELECT * FROM customers WHERE name = '" + name + "'"
    cur.execute(query)
    customers = cur.fetchall()
    conn.close()
    return customers