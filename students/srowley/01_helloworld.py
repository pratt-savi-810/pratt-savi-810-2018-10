# range() function: used to iterate over for loops
#   Has 2 parameters:
#   range (stop)
#     stop: number of integers to generate starting from 0.
#   range(start, stop ,step)
#     start: integer starting sequence
#     stop: Generate integer up to but not including stated integer.
#     step: increment between each integer
#
for i in range(25):
    print('hello world')

# a variable is defined by naming the variable and assigning a value.
#  the value is assigned by placing an equal sign after the variable name.

last_name = 'Rowley'
times_to_print = 10

for i in range(times_to_print):
   print((last_name + '^')*times_to_print)

# ****when variables are predefined you need to constantly adjust them. It is better to create reusable functions.****

# a function is defined by using the 'def' keyword
# 'name_expander' is a user defined function, this is reusable code.
# 'input_text, delim, print_times' are keyword arguments, these are mapped with the function arguments
#   this makes the function reusable

def name_expander(input_text, delim, print_times):
    print((input_text+delim)*print_times)

name_expander('pineapple', '@', 5)