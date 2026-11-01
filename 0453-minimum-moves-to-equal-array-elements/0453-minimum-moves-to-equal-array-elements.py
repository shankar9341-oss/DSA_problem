class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minn = min(nums)
        res = 0
        for n in nums:
            res += n - minn
        return res