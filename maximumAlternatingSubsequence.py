def max_alternating_sum(nums):
    n = len(nums)
    
    if n == 1:
        return nums[0]
    
    # Initialize variables to keep track of the maximum alternating sum
    even_sum = 0
    odd_sum = nums[0]
    
    for i in range(1, n):
        # Calculate the new even_sum and odd_sum based on the current element
        new_even_sum = max(even_sum, odd_sum - nums[i])
        new_odd_sum = max(odd_sum, even_sum + nums[i])
        
        even_sum, odd_sum = new_even_sum, new_odd_sum
    
    # Return the maximum alternating sum
    return max(even_sum, odd_sum)

# Take user input for the array of integers
nums = list(map(int, input().split()))

# Call the function and print the result
result = max_alternating_sum(nums)
print(result)
