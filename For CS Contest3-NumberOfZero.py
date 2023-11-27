

#--------------------------------------------------------

#-------------------------------------------------------
def count_zero_subarrays(nums):
    count = 0
    current_count = 0

    for num in nums:
        if num == 0:
            current_count += 1
            count += current_count
        else:
            current_count = 0

    return count

# Get input from the user
nums = list(map(int, input().split()))

# Calculate and print the number of zero-filled subarrays
result = count_zero_subarrays(nums)
print(result)


#---------------------------------------------------------------


#---------------------------------------------------------------
