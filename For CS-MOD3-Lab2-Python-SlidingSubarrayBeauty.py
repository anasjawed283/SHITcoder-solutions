def sliding_subarray_beauty(arr, k, n):
    beauty_values = []

    for i in range(len(arr) - k + 1):
        subarray = arr[i:i+k]
        sorted_subarray = sorted(subarray)
        beauty_values.append(sorted_subarray[n - 1])

    return beauty_values

# User input
arr = list(map(int, input().split()))
k = int(input())
n = int(input())

# Call the function to get the beauty values
result = sliding_subarray_beauty(arr, k, n)

# Output
print(" ".join(map(str, result)))
