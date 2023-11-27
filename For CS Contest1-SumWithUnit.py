
                                                                                                                                    # Note---Important---- one test case was incorrect on litcoder
class Solution:
    def minimum_numbers(self, num, k):
        if num == 0:
            return 0
        for i in range(1, num + 1):
            t = num - k * i
            if t >= 0 and t % 10 == 0:
                return i
        return -1

# Main program
if __name__ == "__main__":
    solution = Solution()
    num = int(input())
    k = int(input())

    result = solution.minimum_numbers(num, k)
    if result == -1:
        print("-1")
    else:
        print(result)
                                                                                                                            