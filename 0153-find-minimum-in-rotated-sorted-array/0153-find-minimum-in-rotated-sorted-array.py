class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        for i in nums:
            return i