# import sys
# def doSomething(inval):
#     #Do Something
#     return outval
# inputVal = input()    
# outputVal = doSomething(input)
# print (output)
                                                                                                                            

def longest_substring_length(s):
    char_index_map = {}  # To store the index of each character in the string
    start = 0  # Starting index of the current substring
    max_length = 0  # Maximum length of substring without repeating characters

    for end in range(len(s)):
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            # If the current character is already in the substring, update the starting index
            start = char_index_map[s[end]] + 1

        # Update the index of the current character
        char_index_map[s[end]] = end

        # Update the maximum length if the current substring is longer
        max_length = max(max_length, end - start + 1)

    return max_length

input_val = input()
output_val = longest_substring_length(input_val)
print(output_val)
