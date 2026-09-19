class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum1 = 0
        min_len = float("inf")
        for right in range(len(nums)):
            sum1 += nums[right]

            while sum1 >= target:
                min_len = min(min_len, right - left + 1)
                sum1 -= nums[left]
                left += 1

        return 0 if min_len == float("inf") else min_len
        
        
    