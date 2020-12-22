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

# print(return_something())

# Fibonacci Sequence with while loop. 
def do_fibonacci_sequence():
    a = 0
    b = 1

    while a < 100:
        print(a, end=", ")
        # This works by using the original variables' values. This matters because the two variables are dependant on each other.
        b, a = a+b, b


# A part of relearning if-statement.
def check_if_larger_than_0(number):
    if not number: return

    number = int(number)

    if number > 0:
        return "Given result of number " + str(number) + " is larger than 0."
    elif number == 0:
        return "Given result of number " + str(number) + " is equal to 0"
    else:
        return "Given result of number " + str(number) + " is not larger than 0."

# given_number_answer = input("Enter a number to see if it is larger than 0 or not: ")
# print(check_if_larger_than_0(given_number_answer))

# Using for loops
def add_the_same_previous_numbers(number_of_rounds, starting_number):
    current_starting_number = starting_number

    for _ in range(number_of_rounds):
        old_starting_number_string = str(current_starting_number)
        
        current_starting_number *= 2
        new_starting_number_string = str(current_starting_number)

        print(old_starting_number_string + " plus " + old_starting_number_string + " is " + new_starting_number_string)

# add_the_same_previous_numbers(5, 5)

# Testing out more about loops
def loop_test():
    a_number = 1
    while a_number < 10:
        print(a_number)
        a_number += 1
        if a_number == 10:
            break
    # The else block occurs when there are no break statements that occured for the loop on top of it.
    else:
        print("Nothing left for this loop m8")

# loop_test()