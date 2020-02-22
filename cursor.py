#### This is to insert records into your mysql database using python ####
import pymysql.cursors
import random

connection = pymysql.connect (host = 'localhost',
                              user = 'root',
                              password = '',
                              db = 'first_db',
                              charset = 'utf8mb4',
                              cursorclass = pymysql.cursors.DictCursor)

with connection.cursor() as cursor:


    #sql_cmd = 'INSERT into student (age, stu_name, email, address) VALUES ("12", "Saheed", "saheed@mouthodour.com", "Dubai") '
    
#### We are about to open a file containing names #######
    filename = "/Users/doo/Documents/PythonTraining/name.csv"
    raw_data = open(filename, "r").read()

    ### Split names line by line ###
    for name in raw_data.splitlines():

        ### Split each individual line into First name and Last name ###
        f_name, l_name = name.split()

        #####concatenate @yahoo.com to the first 4 letters of the first and lastname#####
        base_email = "@yahoo.com"
        user_mail  = f_name[:4] + l_name[:4] + base_email

        ###generate random numbers for age####
        user_age = random.randrange(10, 50)

        print(f"Firstname - {f_name}, Lastname - {l_name}, Age - {user_age}  Email - {user_mail}" )
        
        #sql_cmd = f'INSERT into customer (stu_name, age, address, email) values ("{name}", "{user_age}", "Dubai", "{user_mail}") '

        #cursor.execute(sql_cmd)
        #connection.commit()

