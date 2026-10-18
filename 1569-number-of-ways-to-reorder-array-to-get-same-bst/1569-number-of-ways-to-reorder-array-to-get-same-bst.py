class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7

        def dfs(nums):
            n = len(nums)
            if n <= 2: return 1
            left = []
            right = []

            for i in range(1, n):
                if nums[i] < nums[0]:
                    left.append(nums[i])
                else: 
                    right.append(nums[i])

            return (dfs(left) * dfs(right) *comb(n-1, len(left))) % MOD

        return (dfs(nums) - 1) % MOD