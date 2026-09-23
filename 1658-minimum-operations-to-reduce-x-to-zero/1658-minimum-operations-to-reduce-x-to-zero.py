class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        sum1 = sum(nums) - x
        max_len = -1
        curr = 0
        left = 0
        for right in range(len(nums)):
            curr += nums[right]
            while left <= right and sum1 < curr:
                curr -= nums[left]
                left += 1
            
            if curr == sum1:
                max_len = max(max_len, right - left + 1)

        return len(nums) - max_len if max_len != - 1 else -1