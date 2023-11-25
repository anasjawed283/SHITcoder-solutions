def candies_steps(target, candies):
    candies.sort()
    steps = 0

    while candies[0] < target:
        combined_sweetness = candies[0] + 2 * candies[1]
        candies = [combined_sweetness] + candies[2:]
        candies.sort()
        steps += 1

    return steps

# Input
target_sweetness = int(input())
candies_list = list(map(int, input().split()))

# Output
result = candies_steps(target_sweetness, candies_list)
print(result)
