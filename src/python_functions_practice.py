calendar = {
    1: "January", 
    2: "February", 
    3: "March", 
    4: "April", 
    5: "May",
    6: "June", 
    7: "July", 
    8: "August", 
    9: "September",
    10: "October"
}



def return_10():
    return 10

def add(number1 , number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

def length_of_string(test_string):
    return len(test_string)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(result1, result2):
    return int(result1) + int(result2)

def number_to_full_month_name(month):
    return calendar[month]

def number_to_short_month_name(month):
    short_name = number_to_full_month_name(month)
    return short_name[0:3]

def volume_of_cube(number):
    cube_volume = number*number*number
    return cube_volume

def reverse_string(string):
    return string [::-1]

def fahrenheit_to_celsius(fahrenheit_temp):
    celsius_temp = (fahrenheit_temp - 32) * (5/9)
    return celsius_temp