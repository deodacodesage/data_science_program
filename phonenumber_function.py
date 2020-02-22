def phone_func(phone_numbers):
    str_number = str(phone_numbers)
    action = str_number.replace("+234", "0")
    print(action)

phone_func("+2348035606744")
