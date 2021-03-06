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

# Learning about the continue statement.
# The continue statement is used when you want to continue with the next iteration of loop, rather than for everything else underneath to be executed.

def loop_test2():
    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found an odd number", num)

# loop_test2()

# Learning about the pass statement.
# If you don't use pass, things that requires an indentation will give an error: IndentationError: expected an indented block

def passing_this():
    pass

# passing_this()

# Definding a function. (I was already doing this :DDD)
# Use the symbol def followed by the function name, then parantheses with arugments in it.

def function_example_with_return():
    return "This is da returning string."

# print(function_example_with_return())

# Default argument values:

def function_with_default_args(defaultArgument = "Default Argument"):
    """
    With this default argument, you would not need to pass in the argument required to run the function.
    And you will not get an error :D.
    """

    print(defaultArgument)

# function_with_default_args()

# Important Note: if you made a default argument to be a mutable object and changes it inside the function, the default will be the same
# for subsequent calls.

# If you don't want this to happen then do this:
def function_with_default_args2(defaultList = None):
    if defaultList == None:
        defaultList = []
    # The rest of your code...

# Keyword argument:
# function_with_default_args2(defaultList = [])

# An argument like this: *argument means that it will accept tuples
# An argument like this: **argument measn that it will accept dictionaries.

def do_a_play(*lines, **characters):
    for line in lines:
        print(line)

    print("-" * 20)

    for character_type in characters:
        print(character_type + ": " + characters[character_type])

# You would call this function like this:
# do_a_play("Hello there.", "General Kenobi...", the_jedi = "Obiwan Kennobi", the_general = "General Grievous")

"""
A function definition may look like this:

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
"""

# Seperating items.
def list_items(*items, seperator = ", "):
    print(seperator.join(items))

# list_items("Hello", "World", seperator="; ")

# Unpacking a list.
# print(*[3, 5])

# lambda expression:
def increment(incremented_by):
    return lambda funcObject: funcObject + incremented_by

# increment1 = increment(10)
# print(increment1(1))

# A function documentation:
def say_words(*words_to_say):
    """
    Parameter:
    words_to_say: string
    """

    for word in words_to_say:
        print(word)

# print(say_words.__doc__)

# Function annotations:
# This is completely optional, it is like documenting but more extreme.

def annotation_example(hello: str = "Hello") -> int:
    print(annotation_example.__annotations__)
    return len(hello)

# annotation_example()

# Testing Python List stuff.
# testList = ["One", "Two", "Three"]
# listToExtend = ["Four", "Five"]
# testList.extend(listToExtend)
# print(testList)

# numbersTo10 = [for x in range(11)]
# print(numbersTo10) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

test = [x+x for x in range(10)]
# print(test)

testTuple = 1, 2, "hi"
# print(testTuple[0])

testSet = set(["hi", "hi", "hello", "hello"])
# print(testSet) -> ["hi", "hello"]

import Fibonacci
# Fibonacci.fib(20)