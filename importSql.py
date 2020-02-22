#### This is to insert records into your mysql database using python ####
import pymysql.cursors
import random

connection = pymysql.connect (host = 'localhost',
                              user = 'root',
                              password = '',
                              db = 'first_db',
                              charset = 'utf8mb4',
                              cursorclass = pymysql.cursors.DictCursor)

# with connection.cursor() as cursor:

#To insert a single row inside a table
#sql_cmd = 'INSERT into student (age, stu_name, email, address) VALUES ("12", "Saheed", "saheed@mouthodour.com", "Dubai") '
   
   ###insert multiple rows from file#####

    
# #### We are about to open a file containing names #######
#     filename = "/Users/doo/Documents/PythonTraining/name.csv"
#     raw_data = open(filename, "r").read()

#     ### Split names line by line ###
#     for name in raw_data.splitlines():

#         ### Split each individual line into First name and Last name ###
#         f_name, l_name = name.split()

#         #####concatenate @yahoo.com to the first 4 letters of the first and lastname#####
#         base_email = "@yahoo.com"
#         user_mail  = f_name[:4] + l_name[:4] + base_email
       
#         user_age = random.randrange(10, 50)

#         print(f"Firstname - {f_name}, Lastname - {l_name}, Age - {user_age}  Email - {user_mail}" )
        
#         sql_cmd = f'INSERT into customer (fname, lname, mail, age) values ("{f_name}", "{l_name}", "{user_mail}", {user_age}) '

#         cursor.execute(sql_cmd)
#         connection.commit()

#####INSERT MULTIPLE ROWS IN PRODUCT TABLE###
with connection.cursor() as cursor:
    
    prod_name = ["book", "iron", "pen", "knife", "board", "table", "roof"]
    prod_prices = [200, 450, 350, 400, 600, 1200, 550]
    prod_weight = ["60g", "44g", "55kg", "100g", "5g", "75g", "10kg"]

    for product in zip (prod_name, prod_prices, prod_weight):

        name = product[0]
        price = product[1]
        weight = product[2]


        sql_cmd = f'INSERT into product (name, price, weight) values ("{name}", "{price}", "{weight}")'
        print(sql_cmd)

        cursor.execute(sql_cmd)
        connection.commit()
