# import sys
# def doSomething(inval):
#     #Do Something
#     return outval
# inputVal = input()    
# outputVal = doSomething(input)
# print (output)


import sys

def findMaxLength(nums):
    # Create a hashmap to store the running sum and its first occurrence index
    sum_index_map = {0: -1}
    
    max_length = 0
    current_sum = 0
    
    for i in range(len(nums)):
        # Update the running sum
        current_sum += 1 if nums[i] == 1 else -1
        
        # Check if the current sum has occurred before
        if current_sum in sum_index_map:
            # Update the maximum length if necessary
            max_length = max(max_length, i - sum_index_map[current_sum])
        else:
            # If the current sum is encountered for the first time, store its index
            sum_index_map[current_sum] = i
    
    return max_length

# Input
input_val = list(map(int, input().split()))

# Perform the task
output_val = findMaxLength(input_val)

# Output
print(output_val)

                                                                                                                            