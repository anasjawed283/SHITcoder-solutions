=def common_child(s1, s2):
    # Initialize a 2D list to store the length of common child strings
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Populate the 2D list with the length of common child strings
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The bottom-right cell of the 2D list contains the length of the longest common child
    return dp[len(s1)][len(s2)]

# Take user input for two strings
s1 = input()
s2 = input()

# Call the function and print the result
result = common_child(s1, s2)
print(result)
