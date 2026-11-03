class Solution:
    def minMoves(self, nums: List[int]) -> int:
        res = 0
        m = max(nums)
        for n in nums:
            res += m - n
        return res