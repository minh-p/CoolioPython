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
    my_string = "This is my lovely string."
    return my_string[0:-5]

print(return_something())