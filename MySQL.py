#conda install -c conda-forge mysql-connector-python=2.2.2

import mysql.connector
import pandas as pd


def read_db(sql, con):
        return pd.read_sql(sql, con)

cnx = mysql.connector.connect(host='hostname', user='user', passwd='password', database='databasename')

q_products = ("SELECT product_id, category, sub_category, brand, seller FROM products;")

products = read_db(q_products, cnx)

q_orders = ("SELECT order_id, customer_id, total, shipping_price, city, state, status, order_date, last_update FROM orders;")

orders = read_db(q_orders, cnx)

q_orderitem = ("SELECT id, order_id, product_id, selling_price FROM orderitem;")

orderitem = read_db(q_orderitem, cnx)

products.to_csv(".\products.csv", sep='\t', index = False)
orders.to_csv(".\orders.csv", sep='\t', index = False)
orderitem.to_csv(".\orderitem.csv", sep='\t', index = False)

cnx.close()