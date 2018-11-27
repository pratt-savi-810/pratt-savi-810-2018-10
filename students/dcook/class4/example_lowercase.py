some_string = ‘ABC’
some_string_list = [‘A’,’B’,’C’]

def make_lower_case(input_string):
	return input_string.lower()
	# print(input_string.lower())
	# print(‘end function’)
my_string_lower = make_lower_case(some_string)
print(my_string_lower)

def make_lowerCase_list(input_list):
	output_list = []
	for i in input_list:
		output_list.append(i.lower())
	return output_list
my_lower_list = make_lowerCase_list(some_string_list)
print(my_lower_list)
