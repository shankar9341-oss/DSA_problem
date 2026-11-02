class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        m = nums[len(nums) // 2]
        res = 0
        for n in nums:
            res += abs(n - m)
        return res
