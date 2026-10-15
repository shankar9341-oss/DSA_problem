class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            curr = set()
            for j in range(i, len(nums)):
                curr.add(nums[j])
                res += len(curr) ** 2

        return res