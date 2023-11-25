def kth_smallest_trimmed_number(nums, queries):
    answer = []
    for query in queries:
        k, trim = query
        trimmed_nums = [num[-trim:] for num in nums]
        sorted_nums = sorted(trimmed_nums)
        kth_smallest = sorted_nums[k - 1]
        index = trimmed_nums.index(kth_smallest)
        answer.append(index)
    return answer

# Example usage
nums = input().split()
n_queries = int(input())
queries = [list(map(int, input().split())) for _ in range(n_queries)]
print(*kth_smallest_trimmed_number(nums, queries))