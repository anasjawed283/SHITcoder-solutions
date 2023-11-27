def is_balanced(string):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    
    for char in string:
        if char in brackets.keys():  # Opening bracket
            stack.append(char)
        elif char in brackets.values():  # Closing bracket
            if not stack or brackets[stack.pop()] != char:
                return "NO"
    
    return "YES" if not stack else "NO"

# Get input from the user
input_strings = input().split(',')

# Process each string and print the result
for input_str in input_strings:
    result = is_balanced(input_str.strip())
    print(result)
