class Solution:
    def twoEggDrop(self, eggs: int, floors: int) -> int:
        dp = [float('inf')] * (floors + 1)
        dp[0] = 0

        for floor in range(1, floors + 1):
            for drop_floor in range(1, floor + 1):
                dp[floor] = min(dp[floor], 1 + max(drop_floor - 1, dp[floor - drop_floor]))

        return dp[floors]

    def find_f(self, eggs, floors):
        low, high = 1, floors
        result = -1

        while low <= high:
            mid = (low + high) // 2
            drops_required = self.twoEggDrop(eggs, mid)

            if drops_required <= floors:
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result

# Example usage
solution = Solution()
eggs = int(input())
floors = int(input())
result = solution.find_f(eggs, floors)
print(result)
