import phonenumbers
from phonenumbers import carrier


def check_number(number):
    country_format = phonenumbers.format_number(phonenumbers.parse(
        number, "NG"), phonenumbers.PhoneNumberFormat.INTERNATIONAL)

    number_profile = phonenumbers.parse(country_format, "NG")

    telco = repr(carrier.name_for_number(number_profile, "en")) 

    print ("Country Format: {} \nNumber Profile: {}\nTelco: {}".format(
        country_format, number_profile, telco.strip("'")))

check_number("08035606744")   