def mix_the_array(n, m, operations):
    arr = [0] * (n + 1)

    for op in operations:
        start, end, value = op
        arr[start - 1] += value
        arr[end] -= value

    max_value = 0
    current_value = 0

    for i in arr:
        current_value += i
        max_value = max(max_value, current_value)

    return max_value

# User input
n = int(input())
m = int(input())

operations = []
for _ in range(m):
    op = list(map(int, input().split()))
    operations.append(op)

# Call the function to get the result
result = mix_the_array(n, m, operations)

# Output
print(result)
