# import sys
# def doSomething(inval):
#     #Do Something
#     return outval
# inputVal = input()    
# outputVal = doSomething(input)
# print (output)

import sys

def analyze_composition(email_address):
    total_characters = len(email_address)
    uppercase_count = sum(1 for char in email_address if char.isupper())
    lowercase_count = sum(1 for char in email_address if char.islower())
    digit_count = sum(1 for char in email_address if char.isdigit())
    symbol_count = total_characters - (uppercase_count + lowercase_count + digit_count)

    uppercase_percentage = (uppercase_count / total_characters) * 100
    lowercase_percentage = (lowercase_count / total_characters) * 100
    digit_percentage = (digit_count / total_characters) * 100
    symbol_percentage = (symbol_count / total_characters) * 100

    return f"{uppercase_percentage:.3f}%\n{lowercase_percentage:.3f}%\n{digit_percentage:.3f}%\n{symbol_percentage:.3f}%"

# Input
input_val = input()

# Perform the task
output_val = analyze_composition(input_val)

# Output
print(output_val)

                                                                                                                            