def phone_func(*args):
    phone_numbers = args
    result_list = []
    for number in phone_numbers:
        string = str(number)
        replaced = string.replace("+234", "0")
        replaced = replaced + " \n"
        result_list.append(replaced)
    print(result_list)
    print("This will be on a \n New line")

phone_func("+2348035606744" , "+2348027127361")
