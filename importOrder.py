import pymysql.cursors
import random

connection = pymysql.connect (host = 'localhost',
                              user = 'root',
                              password = '',
                              db = 'first_db',
                              charset = 'utf8mb4',
                              cursorclass = pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    for prod in range(9):
        cust_id  = random.randrange(1, 23)
        prod_id = random.randrange(1, 8)
        qty = random.randrange(50, 100)
        #date = "2020-02-26"

        print(f"Customer ID - {cust_id}, Product ID - {prod_id}, Quantity - {qty}" )

        sql_cmd = f'INSERT into orders (cust_id, prod_id, qty, order_date) values ("{cust_id}", "{prod_id}", "{qty}", "{2020-02-26}")'

        cursor.execute(sql_cmd)
        connection.commit()
