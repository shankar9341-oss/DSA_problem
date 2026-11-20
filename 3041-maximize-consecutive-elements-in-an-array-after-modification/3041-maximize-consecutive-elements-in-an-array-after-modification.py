class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        res = [0] * (max(nums)+2)
        for n in nums:
            res[n+1] = max(res[n+1], res[n] + 1)
            res[n] = max(res[n], res[n-1] + 1)

        return max(res)