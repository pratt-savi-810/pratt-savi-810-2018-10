some_string = 'ABC'
some_string_list = ['ABC', 'MACARONI', 'TABLE CLOTHE']

def make_lower_case(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item.lower())

    return output_list

my_strings_lower = make_lower_case(some_string_list)

print(my_strings_lower)