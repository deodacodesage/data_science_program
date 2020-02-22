#### We are about to open a file containing names #######
import random
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
    age = random.randrange(10, 50)

    print(f"Firstname - {f_name}, Lastname - {l_name}, Age - {age}  Email - {user_mail}" )


