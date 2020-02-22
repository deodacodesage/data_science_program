def phone_func(*args):
    phone_numbers = args
    result_list = []
    for number in phone_numbers:
        string = str(number)
        replaced = string.replace("+234", "0")
        result_list.append(replaced)


    
variable = phone_func("+2348035606744" , "+2348027127361")
print (variable)
