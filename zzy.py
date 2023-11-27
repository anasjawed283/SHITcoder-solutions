def zigzag_sequence(arr):
    # Remove duplicates and sort the array
    unique_sorted_arr = sorted(set(arr))

    # Determine the length of the array and calculate the index for the zigzag sequence
    n = len(unique_sorted_arr)
    k = (n + 1) // 2

    # Split the array into two halves
    first_half = unique_sorted_arr[:k]
    second_half = unique_sorted_arr[k:]

    # Create the zigzag sequence
    zigzag_seq = []
    for i in range(k):
        zigzag_seq.append(first_half[i])
        if i < len(second_half):
            zigzag_seq.append(second_half[i])

    # Perform pair swaps
    for i in range(1, len(zigzag_seq) - 1, 2):
        zigzag_seq[i], zigzag_seq[i + 1] = zigzag_seq[i + 1], zigzag_seq[i]

    return zigzag_seq

# Get input from the user
n = int(input())
arr = list(map(int, input().split()))

# Get the lexicographically smallest zigzag sequence
result = zigzag_sequence(arr)

# Print the output
print(" ".join(map(str, result)))
