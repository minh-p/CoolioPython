"""
This is my first Python script after a while.
12/20/2020
Huy Minh Pham

"""

def get_the_sum_of_numbers(*numbers):
    current_sum_of_number = 0

    for number in numbers:
        current_sum_of_number += number
    
    return current_sum_of_number

def return_something():
    random_list = [1, "string", 2, None]

    return random_list

print(return_something())

def do_fibonacci_sequence():
    a = 0
    b = 1

    while a < 100:
        print(a, end=", ")
        b, a = a+b, b

do_fibonacci_sequence()