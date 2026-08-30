class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min1 = nums.index(min(nums))
        max1 = nums.index(max(nums))
        left = min(min1, max1)
        right = max(min1, max1)
        
        return min(right + 1, len(nums) - left, left + 1 + len(nums) - right)
